
var goalDay = '2019/06/31 00:00:00'

   var timerId = 0;
   timerId = setInterval(function() {
     var t = Date.parse(goalDay) - Date.parse(new Date());
     if (t < 0) {
       $(".days").text("0");
       $(".hours").text("0");
       $(".minutes").text("0");
       $(".seconds").text("0");
       clearInterval(timerId);
     } else {
       var seconds = Math.floor((t / 1000) % 60);
       var minutes = Math.floor((t / 1000 / 60) % 60);
       var hours = Math.floor((t / (1000 * 60 * 60)) % 24);
       var days = Math.floor(t / (1000 * 60 * 60 * 24));
       $(".days").text(days);
       $(".hours").text(hours);
       $(".minutes").text(minutes);
       $(".seconds").text(seconds);
     }
   }, 2000);
