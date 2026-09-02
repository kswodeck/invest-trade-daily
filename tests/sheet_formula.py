"""A very small Google Sheets formula evaluator, for testing the scorecard.

The Performance tab's figures are spreadsheet formulas, so nothing in the test
suite could reach them: a wrong criterion or a range pointing one column off
would render fine, publish fine, and simply report the wrong number — which is
exactly the class of bug that put 32 "closed" trades on a sheet holding 10.

This evaluates the subset `publish_sheets.cumulative_rows` actually emits —
COUNTIF(S), SUMIFS, AVERAGEIFS, MAXIFS, MINIFS, IFERROR, CONCATENATE and
arithmetic over open-ended column ranges — against a rendered detail table, so
the assertions in the tests are about the numbers a reader would see.

Not a spreadsheet engine. It knows nothing it is not shown.
"""

from __future__ import annotations

import ast
import re
from typing import Any


class _Error:
    """Propagating #DIV/0!, so IFERROR has something to catch.

    Python raises on division by zero; a spreadsheet returns an error value
    that flows through the rest of the expression. Mimicking that is what lets
    `IFERROR(a/b, "—")` be evaluated with ordinary eager argument evaluation.
    """

    def _propagate(self, *_args: Any) -> "_Error":
        return self

    __add__ = __radd__ = __sub__ = __rsub__ = _propagate
    __mul__ = __rmul__ = __truediv__ = __rtruediv__ = _propagate
    __neg__ = __pos__ = _propagate

    def __repr__(self) -> str:  # pragma: no cover - debugging aid
        return "#ERROR!"

    def __bool__(self) -> bool:
        return False


ERROR = _Error()

RANGE = re.compile(r"\$([A-Z]+)\$(\d+):\$([A-Z]+)\b")


def _col_index(letters: str) -> int:
    index = 0
    for char in letters:
        index = index * 26 + (ord(char) - ord("A") + 1)
    return index - 1


def _to_number(value: Any) -> float | None:
    if isinstance(value, bool) or value is None or value == "":
        return None
    if isinstance(value, (int, float)):
        return float(value)
    return None


def _matches(value: Any, criterion: Any) -> bool:
    """One cell against one COUNTIF-style criterion."""
    if isinstance(criterion, (int, float)) and not isinstance(criterion, bool):
        number = _to_number(value)
        return number is not None and number == float(criterion)

    text = str(criterion)
    if text == "<>":
        return value not in ("", None)
    for operator in (">=", "<=", "<>", ">", "<", "="):
        if text.startswith(operator):
            operand = text[len(operator):]
            number, cell = _to_number(_coerce(operand)), _to_number(value)
            if number is None:  # a text comparison, e.g. <>"pending"
                return (str(value) != operand) if operator == "<>" else (str(value) == operand)
            if cell is None:
                return False
            return {
                ">=": cell >= number, "<=": cell <= number, ">": cell > number,
                "<": cell < number, "=": cell == number, "<>": cell != number,
            }[operator]

    if "*" in text:
        pattern = "^" + ".*".join(re.escape(part) for part in text.split("*")) + "$"
        return re.match(pattern, str(value), re.IGNORECASE) is not None
    return str(value).strip().lower() == text.strip().lower()


def _coerce(text: str) -> Any:
    try:
        return float(text)
    except ValueError:
        return text


class Sheet:
    """A rendered detail table, addressable the way the formulas address it."""

    def __init__(self, rows: list[list[Any]], first_row: int) -> None:
        self.rows = rows
        self.first_row = first_row

    def column(self, letters: str, start_row: int) -> list[Any]:
        index = _col_index(letters)
        offset = start_row - self.first_row
        return [row[index] if index < len(row) else ""
                for row in self.rows[max(offset, 0):]]

    # -- functions ---------------------------------------------------------

    @staticmethod
    def _pairs(args: tuple) -> list[tuple[list[Any], Any]]:
        return [(args[i], args[i + 1]) for i in range(0, len(args) - 1, 2)]

    def _mask(self, criteria: tuple) -> list[bool]:
        pairs = self._pairs(criteria)
        length = max(len(rng) for rng, _ in pairs)
        return [all(_matches(rng[i] if i < len(rng) else "", crit) for rng, crit in pairs)
                for i in range(length)]

    def COUNTIF(self, rng: list[Any], criterion: Any) -> float:
        return float(sum(1 for cell in rng if _matches(cell, criterion)))

    def COUNTIFS(self, *args: Any) -> float:
        return float(sum(self._mask(args)))

    def _selected(self, values: list[Any], criteria: tuple) -> list[float]:
        mask = self._mask(criteria)
        out = []
        for i, keep in enumerate(mask):
            if not keep:
                continue
            number = _to_number(values[i] if i < len(values) else "")
            if number is not None:
                out.append(number)
        return out

    def SUMIFS(self, values: list[Any], *criteria: Any) -> float:
        return float(sum(self._selected(values, criteria)))

    def AVERAGEIFS(self, values: list[Any], *criteria: Any) -> Any:
        picked = self._selected(values, criteria)
        return sum(picked) / len(picked) if picked else ERROR

    def MAXIFS(self, values: list[Any], *criteria: Any) -> Any:
        picked = self._selected(values, criteria)
        return max(picked) if picked else ERROR

    def MINIFS(self, values: list[Any], *criteria: Any) -> Any:
        picked = self._selected(values, criteria)
        return min(picked) if picked else ERROR

    @staticmethod
    def IFERROR(value: Any, fallback: Any = "") -> Any:
        return fallback if isinstance(value, _Error) else value

    @staticmethod
    def CONCATENATE(*parts: Any) -> str:
        return "".join(
            f"{part:g}" if isinstance(part, float) else str(part) for part in parts)

    @staticmethod
    def _div(left: Any, right: Any) -> Any:
        if isinstance(left, _Error) or isinstance(right, _Error):
            return ERROR
        try:
            return left / right
        except (ZeroDivisionError, TypeError):
            return ERROR

    # -- evaluation --------------------------------------------------------

    def evaluate(self, formula: str) -> Any:
        """Evaluate one cell. Non-formula values come back unchanged."""
        if not isinstance(formula, str) or not formula.startswith("="):
            return formula

        expression = RANGE.sub(
            lambda m: f'_column("{m.group(1)}", {m.group(2)})', formula[1:])
        tree = ast.parse(expression, mode="eval")
        tree = _SafeDivision().visit(tree)
        ast.fix_missing_locations(tree)

        namespace = {
            name: getattr(self, name) for name in
            ("COUNTIF", "COUNTIFS", "SUMIFS", "AVERAGEIFS", "MAXIFS", "MINIFS",
             "IFERROR", "CONCATENATE")
        }
        namespace["_column"] = self.column
        namespace["_div"] = self._div
        return eval(compile(tree, "<formula>", "eval"), {"__builtins__": {}}, namespace)


class _SafeDivision(ast.NodeTransformer):
    """Route `/` through `_div`, so a zero denominator yields ERROR not a raise."""

    def visit_BinOp(self, node: ast.BinOp) -> ast.AST:
        self.generic_visit(node)
        if isinstance(node.op, ast.Div):
            return ast.Call(func=ast.Name(id="_div", ctx=ast.Load()),
                            args=[node.left, node.right], keywords=[])
        return node
