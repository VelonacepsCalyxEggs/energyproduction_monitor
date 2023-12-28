document.getElementById('exitBut').onclick = function () {   
    eel.logout()
    eel.shutdownServer()    
        console.log('Exiting...')                 

  }
