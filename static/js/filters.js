/*<!-- Function for filter objects properly -->*/

  $('#makes').change(function() {
    var makeValue = $('#makes').val();
    var path = window.location.pathname;
    path += '?make=' + makeValue;
    window.location.href = path;
  });
  $('#models').change(function(){
    var makeValue = $('#makes').val();
    var modelValue = $('#models').val();
    var path = window.location.pathname;
    path += '?make=' + makeValue + '&model=' + modelValue;
    window.location.href = path;
  });

  $('#fuels').change(function() {
    var makeValue = $('#makes').val();
    var modelValue = $('#models').val();
    var fuelValue = $('#fuels').val();
    var path = window.location.pathname;
    path += '?'
    if(makeValue) {
        path += path.endsWith('?') ? 'make=' :  '&make=';
        path += makeValue;
     }
    if(fuelValue) {
      path += path.endsWith('?') ? 'fuel=' :  '&fuel=';
      path += fuelValue;
     }
    if(modelValue) {
      path += path.endsWith('?') ? 'model=' :  '&model=';
      path += modelValue
    }
  //  path += '?make=' + makeValue + '&fuel=' + fuelValue + '&model=' + modelValue ;
    window.location.href = path;
  });
