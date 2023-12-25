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
    console.log(loginparsed)
    console.log(passwordparsed)

    eel.login(loginparsed,passwordparsed)().then(function (loggedin) {
    if (loggedin == 1) {
        console.log('balls')
    }
    else {
        window.location.href = 'http://localhost:55045/login.html'
    }
 })
  })
  .catch(error => {
    // Handle any errors that occurred during the fetch
    console.error('Fetch error:', error);
  });
    })