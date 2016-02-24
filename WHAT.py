#! /usr/bin/env python

# WiFi Auditing Tool
# A multi-capable tool for automating WiFi attacks and moving data around

from Tkinter import *
import subprocess

window = Tk()
window.title ( 'WiFi Hacking Attack Tool v1.0' )
WINDOW_SIZE = "600x400"
img = PhotoImage( file = '/root/WHAT/Wifi_Logo.gif' )
small_img = PhotoImage.subsample( img , x = 3 , y = 3 )
label = Label( window , image = small_img , bg = 'red')
label.grid(row=0,column=2) 

btn_end = Button( window , text = 'Close' , command=exit )
btn_end.grid(row=10,column=2)

def runShellScript():
	import subprocess
	subprocess.call(['/root/WHAT/./SURVEY-LAUNCH.sh'])

btn_scn = Button( window , text = 'Survey' , command=runShellScript , width = 15 )
btn_scn.grid(row=1,column=0 ) 

def runShellScript1():
	import subprocess
	subprocess.call(['/root/WHAT/./EXPLOIT-LAUNCH.sh'])

btn_pcp = Button( window , text = 'Exploit' , command=runShellScript1 , width = 15 )
btn_pcp.grid(row=1,column=1)

def runShellScript2():
	import subprocess
	subprocess.call(['/root/WHAT/./GEO-LAUNCH.sh'])

btn_pcp = Button( window , text = 'Geolocation' , command=runShellScript2 , width = 15 )
btn_pcp.grid(row=1,column=2)

def runShellScript3():
	import subprocess
	subprocess.call(['/root/WHAT/./COMMS-LAUNCH.sh'])

btn_ovp = Button( window , text = 'Communications' , command=runShellScript3 , width = 15 )
btn_ovp.grid(row=1,column=3)

def runShellScript4():
	import subprocess
	subprocess.call(['/root/WHAT/./FOLDERS-LAUNCH.sh'])

btn_dad = Button( window , text = 'Admin' , command=runShellScript4 , width = 15 )
btn_dad.grid(row=1,column=4)

window.mainloop()

