/*! app bundle */
var e={SEARCH:"/api/property_sales/",DETAIL:"/api/property_sales/detail/",
LOGO:"/static/logo.svg",MAP:"/api/map_tiles/"};
function load(){return fetch(e.SEARCH+"?county="+c)}
