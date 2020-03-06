/*<!-- Function for filter objects properly -->*/

  $('#makes').change(function() {
    var makeValue = $('#makes').val();
    var path = window.location.pathname;
    path += '?make=' + makeValue;
    console.log(path);
    window.location.href = path;
  });
  $('#models').change(function(){
    var makeValue = $('#makes').val();
    var modelValue = $('#models').val();
    var path = window.location.pathname;
    path += '?make=' + makeValue + '&model=' + modelValue;
    window.location.href = path;
  });

  function filterCars(){
    var makeValue = $('#makes').val();
    var modelValue = $('#models').val();
    var fuelValue = $('#fuels').val();
    var dateValue = $('#dates').val();
    var priceValue = $('#prices').val();
    var category = $('#categories').val();
    var mileage = $('#mileages').val();
    var transmission = $('#transmissions').val();
    console.log(transmission)
    if(transmission == 'None') transmission = ""
    console.log(transmission)

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
    if (dateValue) {

      path += path.endsWith('?') ? 'date=' : '&date=';
      path += dateValue;
    }
    if (priceValue) {

      path += path.endsWith('?') ? 'price=' : '&price=';
      path += priceValue;
    }
    if (category) {

      path += path.endsWith('?') ? 'category=' : '&category=';
      path += category;
    }
    if (mileage) {

      path += path.endsWith('?') ? 'mileage=' : '&mileage=';
      path += mileage;
    }
    if (transmission) {

      path += path.endsWith('?') ? 'transmission=' : '&transmission=';
      path += transmission;
    }
  //  path += '?make=' + makeValue + '&fuel=' + fuelValue + '&model=' + modelValue ;
    window.location.href = path;

  }

  $('#fuels').change(function() {
    filterCars();
  });

  $('#dates').change(function() {

    filterCars();
  });

  $('#prices').change(function() {

    filterCars();
  });
  $("#categories").change(function(){
    filterCars();
  })
  $("#mileages").change(function(){
    filterCars();
  })
  $("#transmissions").change(function(){
    filterCars();
  })

var urlParams = new URLSearchParams(window.location.search);

$(document).ready(function() {
  var urlParams = new URLSearchParams(window.location.search);
  var keys = urlParams.keys();
  for(key of keys) { 
    console.log(key);
    console.log(urlParams.get(key));
    if(key == 'category')
      $('#categories').val(urlParams.get(key));
    else if(key == 'make')
      $('#makes').val(urlParams.get(key));
    else if(key == 'mileage')
      $('#mileages').val(urlParams.get(key));
    else if(key == 'transmission')
      $('#transmissions').val(urlParams.get(key));
    else if(key == 'model')
      $('#models').val(urlParams.get(key));
    else if(key == 'fuel')
      $('#fuels').val(urlParams.get(key));
    else if(key == 'date')
      $('#dates').val(urlParams.get(key));
    console.log()
  }
});


