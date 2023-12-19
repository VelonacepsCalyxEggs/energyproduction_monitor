import eel
import sys
import subprocess

eel.init("C:/Users/ivank/source/repos/energyproduction_monitor/appl/gui") 

@eel.expose
def startup():
    text = "test"
    return text

@eel.expose
def shutdownServer():
    eel._shutdown
    print('goodbye world!')
    subprocess.call("TASKKILL /F /IM chrome.exe", shell=True) # This can have serious reprecussions... and I am too lazy to fix this. Fuck chrome anyway.
    sys.exit()

eel.start('index.html', size=(1024, 512), port=55045)