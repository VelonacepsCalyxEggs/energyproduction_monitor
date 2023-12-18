// Onclick of the button 
document.querySelector("button").onclick = function () {   
    // Call python's random_python function 
    eel.startup()(function(string){                       
      // Update the div with a random number returned by python 
      //document.querySelector("#testchange").innerHTML = string; 
      location.href = "http://localhost:55045/energygraph.html";
    }) 
  }