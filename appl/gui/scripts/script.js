document.addEventListener('DOMContentLoaded', function() {  //проверка скрипта
    console.log('Test 42')

})

document.getElementById('buttonId').onclick = function () { // в idшник вписать id кнопки.
    document.querySelector('form') 
        //e.preventDefault(); чмоня пока не нужна 
    
        var data = {
                name: document.querySelector('input').value,
                comment: document.querySelector('textarea'). value
        }
    
        console.log(data); //sendForm
}


// async function sendForm(data) {
//     const res = await fetch('./feedback.php', {
//         method: 'POST',
//         headers: {'Content-type': 'application/json'},
//         body: JSON.stringify(data)

//     });
//     const result = await res.json();
//     console.log(result)
//     // if (res.status === 201) {
//     //     alert{'Thank you!' ${result.message}}
//     // }
// }