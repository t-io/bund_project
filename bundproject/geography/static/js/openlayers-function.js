//declaring the constructor  
function MapMaker(id) {  
    this.id = id;
    this.map = new OpenLayers.Map(this.id);

    // Layer contains MapBase
    this.layer = new OpenLayers.Layer.WMS( "OpenLayers WMS",
               "http://labs.metacarta.com/wms/vmap0", {layers: 'basic'} );

    //Layer Style
    this.layer_style = OpenLayers.Util.extend({}, OpenLayers.Feature.Vector.style['default']);
        this.layer_style.fillOpacity = 0.2;
        this.layer_style.graphicOpacity = 1;

    //Point Style
    this.style_blue = OpenLayers.Util.extend({}, this.layer_style);
        this.style_blue.strokeColor = "blue";
        this.style_blue.fillColor = "blue";
        this.style_blue.graphicName = "star";
        this.style_blue.pointRadius = 10;
        this.style_blue.strokeWidth = 3;
        this.style_blue.rotation = 45;
        this.style_blue.strokeLinecap = "butt";

    //new Vector Layer for Points
    this.vectorLayer = new OpenLayers.Layer.Vector("Simple Geometry", {style: this.layer_style});

} 

MapMaker.prototype = {  
    createMap: function () { 
        //add backgroundMap
        this.map.addLayer(this.layer);
        
        // add Vectorlayer with Points
        this.map.addLayer(this.vectorLayer);
    },  
    addPoint: function (point_x, point_y) {  
        // create GeometryPoints
        var point = new OpenLayers.Geometry.Point(point_x, point_y);
        //Create FeaturePoint from Geometry
        var pointFeature = new OpenLayers.Feature.Vector(point, null, this.style_blue);
        //add this to the Object VectorLayer
        this.vectorLayer.addFeatures([pointFeature]);
    },
    setCenter: function (point_x, point_y, zoom) {  
        // set center and zoom for the current Map
        this.map.setCenter(new OpenLayers.LonLat( point_x, point_y ), zoom);
    }

    // add Lines on a new VectorLayer


};  