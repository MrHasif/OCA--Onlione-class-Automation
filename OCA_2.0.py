import os
import time
import pyautogui
from easygui import *

#function for choice boxes
def Select(text,title,op1,op2,op3):
	choices=[op1,op2,op3]
	return(choicebox(text,title,choices))

#function for mouse
def mouse(x,y,delay):
	pyautogui.moveTo(x, y, duration=2, tween=pyautogui.easeInOutQuad)
	time.sleep(1)
	pyautogui.click()
	time.sleep(delay)


#whatsapp group
group=Select(text="Select Group",title="Whatapp group",op1="Mobile",op2="ELECTRONICS 2nd Alnoor",op3="Electronics 2nd Year 2021")

#operagx opening delay

gxdelay=Select(text="Select delay",title="OperaGx wait time",op1="60",op2="15",op3="30")

#whatsapp delay

wadelay=Select(text="Select delay",title="Whatsapp wait time",op1="60",op2="15",op3="30")

pdelay=Select(text="Select delay",title="Powerpoint wait time",op1="60",op2="20",op3="30")

#launch gx
os.startfile('C:/Users/MrBABAYEGA/AppData/Local/Programs/Opera GX/launcher.exe') #launch opera gx
time.sleep(int(gxdelay))



pyautogui.write('meet.google.com', interval=0.25)#go to meet
pyautogui.press('enter')
time.sleep(20)

mouse(x=137, y=536,delay=1) #click on create meeting

pyautogui.move(0, 60,duration=1)   #instant meeting
pyautogui.click()
time.sleep(12)

mouse(x=617,y=726,delay=1)#mute video
mouse(x=567,y=728,delay=1)#mute audio
mouse(x=402,y=332,delay=1)#copy link
mouse(x=16,y=207,delay=int(wadelay))#open whatsapp
mouse(x=174,y=112,delay=1)#whatsapp text box

pyautogui.write(str(group), interval=0.25) #Enter group name
time.sleep(1)

mouse(x=224,y=232,delay=1)#select group
mouse(x=615,y=735,delay=1)#chat box

pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste link
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

mouse(x=1130,y=2,delay=1)#click outside

os.startfile('C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE') #start powerpoint
time.sleep(int(pdelay))

mouse(x=340,y=462,delay=1)#open recent powerpoint
















