import eel

eel.init("C:/Users/Student/Music/appl/gui") 


@eel.expose
def startup():
    text = "niggas"
    return(text)


eel.start('index.html', size=(1024,512),  port = 55045) 