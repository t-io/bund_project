//declaring the constructor  
function MapMaker(id) {  
    this.id = id;
    
    this.proj_1 = new OpenLayers.Projection("EPSG:4326");
    this.proj_2 = new OpenLayers.Projection("EPSG:900913");
    
    this.map = new OpenLayers.Map(this.id);
    
    //Autobahn
    this.lines = [];
    
    //Bundesstrße
    this.lines2 = [];

    // BackgroundLayer
    /*
    this.layer = new OpenLayers.Layer.WMS( "OpenLayers WMS",
               "http://labs.metacarta.com/wms/vmap0", {layers: 'basic'} );
    */

    this.osm_mapnik = new OpenLayers.Layer.OSM();

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

    //Line Style Autobahn
    this.style_green = {
        strokeColor: "#B59142",
        strokeOpacity: 0.65,
        strokeWidth: 3
    };
    
    //Line Style Bundesstraße
    this.style_bund = {
        strokeColor: "#FF31D1",
        strokeOpacity: 0.65,
        strokeWidth: 3
    };

    //create new Vector Layer for Points & Lines
    this.vectorLayerPoints = new OpenLayers.Layer.Vector("Points Umgehungsstraßen", {style: this.layer_style});
    this.vectorLayerLines = new OpenLayers.Layer.Vector("Lines Bundesstraßen", {style: this.layer_style});

    this.vectorLayerLines2 = new OpenLayers.Layer.Vector("Lines Autobahn", {style: this.style_bund});
} 

MapMaker.prototype = {  
    createMap: function () { 
        //add backgroundMap
        this.map.addLayer(this.osm_mapnik);

        // add Vectorlayer with Points & Lines
        this.map.addLayer(this.vectorLayerPoints);
        this.map.addLayer(this.vectorLayerLines);
        this.map.addLayer(this.vectorLayerLines2);

        //alert(this.map.getProjection());
    },  
    addPoint: function (point_x, point_y) {  
        // create GeometryPoints
        var point = new OpenLayers.Geometry.Point(point_x, point_y);
        //Create FeaturePoint from Geometry
        var pointFeature = new OpenLayers.Feature.Vector(point, null, this.style_blue);
        //add this to the Object VectorLayer
        this.vectorLayerPoints.addFeatures([pointFeature]);
    },
    createLine: function (pointArray, streettype){
        // create a LineString from a PointArray and push it to an Array
        lineString = new OpenLayers.Geometry.LineString(pointArray).transform(this.proj_1, this.proj_2);
        if(streettype == "AU"){
            this.lines.push(lineString);
        }
        if(streettype == "BU"){
            this.lines2.push(lineString);
        }
        
    },
    showlines: function(){
        // get the Array of LineStrings and add the LineStrings to the VectorLayer
        for (var i = 0; i < this.lines.length; i++){            
            var lineFeature = new OpenLayers.Feature.Vector(this.lines[i], null, this.style_green);
            this.vectorLayerLines.addFeatures([lineFeature]);
            console.log("Autobahn"); 
        }

        for (var i = 0; i < this.lines2.length; i++){            
            var lineFeature2 = new OpenLayers.Feature.Vector(this.lines2[i], null, this.style_bund);
            this.vectorLayerLines2.addFeatures([lineFeature2]);
            console.log("Bundesstraße"); 
        }

    },
    setCenter: function (point_x, point_y, zoom) {  
        // set center and zoom for the current Map
        this.map.setCenter(new OpenLayers.LonLat( parseFloat(point_x), parseFloat(point_y) ).transform(this.proj_1, this.proj_2), parseInt(zoom) );
    },
    panToPoint: function (point_x, point_y, zoom){
        if(this.map.getZoom() != parseInt(zoom)){
            this.map.zoomTo(parseInt(zoom));
        }
        
        lonlat = new OpenLayers.LonLat(point_x, point_y).transform(this.proj_1, this.proj_2);
        this.map.panTo(lonlat);

    }

};  