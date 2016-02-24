#! /usr/bin/env python

# WiFi Auditing Tool Survey
# WiFi and Network Scanning Tools

from Tkinter import *
import subprocess

window = Tk()
window.title ( 'WHAT Survey v1.0' )
WINDOW_SIZE = "600x400"
img = PhotoImage( file = '/root/WHAT/Wifi.gif' )
small_img = PhotoImage.subsample( img , x = 4 , y = 4 )
label = Label( window , image = small_img , bg = 'red')
label.grid(row=0,column=0) 

btn_end = Button( window , text = 'Close' , command=exit )
btn_end.grid(row=10,column=0)

def runShellScript5():
	import subprocess
	subprocess.call(['/root/WHAT/./AIRODUMP-SCAN-LAUNCH.sh'])

btn_scn = Button( window , text = 'Start WiFi Survey' , command=runShellScript5 , width = 15 )
btn_scn.grid(row=1,column=0 ) 

def runShellScript6():
	import subprocess
	subprocess.call(['/root/WHAT/./WASH-SCAN-LAUNCH.sh'])

btn_pcp = Button( window , text = 'WPS Survey' , command=runShellScript6 , width = 15 )
btn_pcp.grid(row=3,column=0)

def runShellScript3():
	import subprocess
	subprocess.call(['/root/WHAT/./AIRODUMP-PCAP-LAUNCH.sh'])

btn_ovp = Button( window , text = 'WiFi Survey (PCAP)' , command=runShellScript3 , width = 15 )
btn_ovp.grid(row=2,column=0)

window.mainloop()

