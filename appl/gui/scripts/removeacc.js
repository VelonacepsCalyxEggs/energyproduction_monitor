document.getElementById('userRemove').onclick = function () {
    var login = document.getElementById('userAdminRemove').value;
    eel.removeUser(login)().then(function (error){
    })
}