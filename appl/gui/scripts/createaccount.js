document.getElementById('userCreate').onclick = function () {
    var login = document.getElementById('userAdmin').value;
    var password = document.getElementById('passwordAdmin').value;
    eel.createNewUser(login,password)().then(function (error){
    })
}