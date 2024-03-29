'use strict';

   var time_in_minutes = 1;
   var current_time = Date.parse(new Date());
   var deadline = new Date(current_time + time_in_minutes*60*1000);
   function time_remaining(endtime){
       var t = Date.parse(endtime) - Date.parse(new Date());
       var seconds = Math.floor( (t/1000) % 60 );
       var minutes = Math.floor( (t/1000/60) % 60 );
       var hours = Math.floor( (t/(1000*60*60)) % 24 );
       var days = Math.floor( t/(1000*60*60*24) );
       return {'total':t, 'days':days, 'hours':hours, 'minutes':minutes, 'seconds':seconds};
   }
   function run_clock(timer, endtime){
       var clock = document.getElementById(timer);
       function update_clock(){
           var t = time_remaining(endtime);

           if (t.minutes < 10 && t.seconds < 10) {
               clock.textContent = '0' + t.minutes + ':' + '0' + t.seconds;
               if (t.minutes < 1) {
                 clock.style.color="red";
               }
           }
           else if (t.minutes < 10) {
               clock.textContent = '0' + t.minutes + ':' + t.seconds;
           }
           else if (t.seconds < 10) {
               clock.textContent = t.minutes + ':' + '0' + t.seconds;
           }
           else {
               clock.textContent = t.minutes + ':' + '0' + t.seconds;
           }
           if (t.total<=0) {
             clearInterval(timeinterval);
             window.location.pathname = '/results';
           }
       }
   update_clock();
   var timeinterval = setInterval(update_clock,1000);
   }
   run_clock("clockdiv", deadline);
