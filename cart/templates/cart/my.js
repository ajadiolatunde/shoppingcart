

function first(){
   console.log("hello world")
}

(function (){
  var i = document.querySelectorAll('input');
  var il = Array.prototype.slice.call(i);
  console.log(i);
        il.forEach(function(elm){
          elm.addEventListener("change", function() {

            console.log(elm.value);
          });


         console.log(elm);
        });
})();

//IIFE
!function () {
  var p = document.getElementById("demop")


  for (let k =0; k<400; k++){

      (function (k) {
        setTimeout(function () {
           p.style.margin = k+"px 0 0 0";
           console.log(k)

         }, 10000);
        })(k);



  }


}();


function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}




function displayFullName() {
    // Creating the XMLHttpRequest object
    var request = new XMLHttpRequest();

    // Instantiating the request object
    request.open("GET", "greet?fname=John&lname=Clark");

    // Defining event listener for readystatechange event
    request.onreadystatechange = function() {
        // Check if the request is compete and was successful
        if(this.readyState === 4 && this.status === 200) {
            // Inserting the response from server into an HTML element
            document.getElementById("result").innerHTML = this.responseText;
        }
    };

    // Sending the request to the server
    request.send();
}
