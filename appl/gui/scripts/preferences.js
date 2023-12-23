document.getElementById('buttonSave').onclick = function () {
    var username = document.getElementById('user').value;
    var ipAddress = document.getElementById('ipAddress').value;
    var port = document.getElementById('port').value;
    var password = document.getElementById('password').value;
    eel.configEdit(username,ipAddress,port,password)().then(function (error) {
        console.log(error)
        if (error == 42) {
            console.log('config is good')
            let errorElement = document.getElementById("error");
            let newItem = document.createElement("p");
            newItem.innerHTML = 'Config saved sucsessfully.'
            newItem.className = "text-success fw-bold"
            errorElement.appendChild(newItem)
        }
        else {
            console.log(error)
            let errorElement = document.getElementById("error");
            let newItem = document.createElement("p");
            newItem.innerHTML = error
            newItem.className = "text-danger fw-bolder"
            errorElement.appendChild(newItem)
        }


    })

}