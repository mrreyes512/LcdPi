#!/usr/bin/python
#Daniel Juenger, github.com/sleeepyjack

from time import sleep
#import Adafruit_CharLCD as LCD
#from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from Menu import Menu

lcd = Adafruit_CharLCDPlate()
menu = Menu()

#The menu can show strings, bash and python expressions

#		     topElement(      Name , Type of content , Lower row content)

top1 = menu.topElement("< System       >", "STRING", "        v")
top2 = menu.topElement("< Network      >", "STRING", "        v")
top3 = menu.topElement("< top3         >", "STRING", "        v")
top4 = menu.topElement("< top4         >", "STRING", "        v")
top5 = menu.topElement("< top5         >", "STRING", "        v")


sub11 = menu.subElement("System>Hostname", "BASH", "hostname")
sub12 = menu.subElement("System>CPU", "PYTHON", 'str(str(psutil.cpu_percent()) + "%")')
sub13 = menu.subElement("System>CPU-Temp.", "BASH", "/opt/vc/bin/vcgencmd measure_temp | cut -d '=' -f2")
sub14 = menu.subElement("System>CPU-Proceses", "BASH", "ps ax | wc -l | tr -d \" \" ")
sub15 = menu.subElement("System>RAM", "PYTHON", 'str(str(psutil.phymem_usage()[3])+"% used")')
sub16 = menu.subElement("System>Kernel", "BASH", "uname -srmo")

sub21 = menu.subElement("Network>SSID", "BASH", "iwconfig wlan0 | grep 'ESSID:' | awk '{print $4}' | sed 's/ESSID://g'")
sub22 = menu.subElement("Network>Signal", "BASH", "iwconfig wlan0 | awk -F'[ =]+' '/Signal level/ {print $7}' | cut -d/ -f1")
sub23 = menu.subElement("Network>Internet", "BASH", "ping -q -w 1 -c 1 www.google.com > /dev/null && echo \"Google Ping: ok\" || echo error")
sub24 = menu.subElement("Network>External", "BASH", "wget -q -O - http://icanhazip.com || echo error")
sub25 = menu.subElement("Network>Internal", "BASH", "ifconfig wlan0 | grep \"inet addr\" | cut -d: -f2 | awk '{print $1}'")



#Adding elements to the menu
menu.addTopElement(top1)
menu.addTopElement(top2)
menu.addTopElement(top3)
menu.addTopElement(top4)
menu.addTopElement(top5)

menu.addSubElement(top1, sub11)
menu.addSubElement(top1, sub12)
menu.addSubElement(top1, sub13)
menu.addSubElement(top1, sub14)
menu.addSubElement(top1, sub15)
menu.addSubElement(top1, sub16)

menu.addSubElement(top2, sub21)
menu.addSubElement(top2, sub22)
menu.addSubElement(top2, sub23)
menu.addSubElement(top2, sub24)
menu.addSubElement(top2, sub25)

color = lcd.TEAL

#initializing display
lcd.clear()
lcd.backlight(color)

#little loading animation
i = 0
lcd.message("LOADING\n")
while(i < 16):
    lcd.message(chr(219))
    sleep(.1)
    i += 1

#starting the menu
menu.startMenu(lcd, color)
