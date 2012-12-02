//declaring the constructor  
function MapMaker(id) {  
    this.id = id;
    this.map = new OpenLayers.Map(this.id);
    this.lines = [];

    // BackgroundLayer
    this.layer = new OpenLayers.Layer.WMS( "OpenLayers WMS",
               "http://labs.metacarta.com/wms/vmap0", {layers: 'basic'} );

    //Layer Style ( at the moment for both layers, can be changed...maybe sometimes..)
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

    //Line Style
    this.style_green = {
        strokeColor: "#00FF00",
        strokeOpacity: 0.7,
        strokeWidth: 6
    };

    //create new Vector Layer for Points & Lines
    this.vectorLayerPoints = new OpenLayers.Layer.Vector("Points Umgehungsstraßen", {style: this.layer_style});
    this.vectorLayerLines = new OpenLayers.Layer.Vector("Lines Bundesstraßen", {style: this.layer_style});

} 

MapMaker.prototype = {  
    createMap: function () { 
        //add backgroundMap
        this.map.addLayer(this.layer);
        
        // add Vectorlayer with Points & Lines
        this.map.addLayer(this.vectorLayerPoints);
        this.map.addLayer(this.vectorLayerLines);
    },  
    addPoint: function (point_x, point_y) {  
        // create GeometryPoints
        var point = new OpenLayers.Geometry.Point(point_x, point_y);
        //Create FeaturePoint from Geometry
        var pointFeature = new OpenLayers.Feature.Vector(point, null, this.style_blue);
        //add this to the Object VectorLayer
        this.vectorLayerPoints.addFeatures([pointFeature]);
    },
    createLine: function (pointArray){
        // create a LineString from a PointArray and push it to an Array
        lineString = new OpenLayers.Geometry.LineString(pointArray);
        this.lines.push(lineString);
    },
    showlines: function(){
        // get the Array of LineStrings and add the LineStrings to the VectorLayer
        for (var i = 0; i < this.lines.length; i++){            
            var lineFeature = new OpenLayers.Feature.Vector(this.lines[i], null, this.style_green);
            this.vectorLayerLines.addFeatures([lineFeature]);
        }

    },
    setCenter: function (point_x, point_y, zoom) {  
        // set center and zoom for the current Map
        this.map.setCenter(new OpenLayers.LonLat( point_x, point_y ), zoom);
    }

};  