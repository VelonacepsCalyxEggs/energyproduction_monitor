
document.getElementById('buttonLogin').onclick = function () {
        var login = document.getElementById('login').value;
        var password = document.getElementById('password').value;
        console.log(login)
        console.log(password)
        var check = 0
    
    eel.login(login,password)().then(function (loggedin) {
        if (loggedin == 1) {
            setTimeout(() => {window.location.href = 'http://localhost:55045/index.html'}, 50)
        }
        else {
            console.log(loggedin)
            let errorElement = document.getElementById("error");
            let newElem = document.createElement('div')
            newElem.innerHTML = 'Invalid login or password'
            errorElement.appendChild(newElem)
        }
     })
    }