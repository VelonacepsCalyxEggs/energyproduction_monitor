document.addEventListener('DOMContentLoaded', function() { 
    fetch('http://localhost:55045/scripts/userdata.json')
  .then(response => {
    // Check if the response is successful
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    // Parse the JSON data
    return response.json();
  })
  .then(data => {
    // Process the JSON data
    passwordparsed = data.login
    loginparsed = data.password
    roleparsed = data.role
    console.log(loginparsed)
    console.log(passwordparsed)
    console.log(roleparsed)

    eel.login(loginparsed,passwordparsed)().then(function (loggedin) {
    if (loggedin == 1) {
        console.log('balls')
    }
    else {
        window.location.href = 'http://localhost:55045/login.html'
    }
    if (roleparsed == 'admin') {

    }
    else {
        var elements = document.getElementsByClassName('adminInt');

        // Convert the HTMLCollection to an array
        var elementsArray = Array.from(elements);

        // Loop through the array and remove each element
        elementsArray.forEach(function(element) {
        element.parentNode.removeChild(element);
        });
    }
 })
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('Fetch error:', error);
  });
    })