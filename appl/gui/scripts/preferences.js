document.getElementById('buttonSave').onclick = function () {
    var username = document.getElementById('user').value;
    var ipAddress = document.getElementById('ipAddress').value;
    var port = document.getElementById('port').value;
    var password = document.getElementById('password').value;
    console.log('IP Address:', username);
    console.log('IP Address:', ipAddress);
    console.log('Port:', port);
    console.log('Port:', password);
    eel.configEdit(username,ipAddress,port,password)

}