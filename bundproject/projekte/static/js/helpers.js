function converToFloat(floatNumber){
	// Convert the NumberString Comma to Point and return Float 
	floatNumber = new String(floatNumber);
	floatNumber = floatNumber.replace(',', '.');

	return parseFloat(floatNumber);
}