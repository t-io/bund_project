function converToFloat(floatNumber){
	// Convert the NumberString Comma to Point and return Float 
	floatNumber = new String(floatNumber);
	floatNumber = floatNumber.replace(',', '.');

	return parseFloat(floatNumber);
}

$(document).ready(function() {
  $(".bt_zoom").click(function() {

	}, function() {
  	  	
		center = $(this).html();

  	  	if(center == "Baden-Württemberg"){
  			map.panToPoint(9.337555, 48.745323, 9);
  		}else if(center == "Bayern"){
  			map.panToPoint(11.661894, 48.947414, 9);
  		}else if(center == "Berlin"){
  			map.panToPoint(13.397631, 52.506669, 12);
  		}else if(center == "Brandenburg"){
  			map.panToPoint(13.531497, 52.360097, 9);
  		}else if(center == "Bremen"){
  			map.panToPoint(8.808172, 53.096978, 12);
  		}else if(center == "Hamburg"){
  			map.panToPoint(10.005336, 53.540792, 12);
  		}else if(center == "Hessen"){
  			map.panToPoint(9.043078, 50.612747, 9);
  		}else if(center == "Mecklenburg-Vorpommern"){
  			map.panToPoint(12.432100, 53.740986, 9);
  		}else if(center == "Niedersachsen"){
  			map.panToPoint(9.292033, 52.705189, 9);
  		}else if(center == "Nordrhein-Westfalen"){
  			map.panToPoint(7.565403, 51.470964, 9);
  		}else if(center == "Rheinland-Pfalz"){
  			map.panToPoint(7.371425, 49.829708, 9);
  		}else if(center == "Saarland"){
  			map.panToPoint(6.956911, 49.372231, 9);
  		}else if(center == "Sachsen"){
  			map.panToPoint(13.366642, 51.030758, 9);
  		}else if(center == "Sachsen-Anhalt"){
  			map.panToPoint(11.664772, 51.996514, 9);
  		}else if(center == "Schleswig-Holstein"){
  			map.panToPoint(9.836789, 54.120664, 9);
  		}else if(center == "Thüringen"){
  			map.panToPoint(10.932847, 50.926550, 9);
  	}
});
});