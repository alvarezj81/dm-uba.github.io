# 12/05/2020
#
# by Sergio Marchio
#
# Zoom Meetings Data Mining Exactas 2020
# El script abre el navegador con el link a la reunion del dia
# Deja la clave en el portapapeles
#
# 2do cuatri 31/08/2020
# 19/09/2020
# update para que se ejecute sin browser!
# 
# 
# https://marketplace.zoom.us/docs/guides/guides/client-url-schemes
# Joining a Meeting:
# Windows/macOS Client: zoommtg://zoom.us/join?confno=123456789&pwd=xxxx
# iOS/Android Client: zoomus://zoom.us/join?confno=123456789&pwd=xxxx
# 
# 
# si se corre con un argumento es para pedirle un dia en especial
# 0 - lunes
# ...
# 5 - sabado 

# actualizado 1 cuat 2021
# curso solo AID pero pongo AA y DM tambien porque qcyo

import datetime
import clipboard
import os
import subprocess
import sys

import pyautogui
import time
import win32gui

zoom_urls = [
    ["lunes - AA", "87938496623", "aa21-lent"],
    ["martes - DM", "84149646096", "dm21-hamp"],
    ["miercoles - (-)", "--", "--"],
    ["jueves - AA", "87938496623", "aa21-lent"],
    ["viernes - DM", "84149646096", "dm21-hamp"],
    ["sabado - AID","88491195346", "aid21-los"]
];

dias = ["lu", "ma", "mi", "ju", "vi", "sa"]

if(len(sys.argv) > 1):
    if(sys.argv[1].isdigit() == True and 0 <= int(sys.argv[1]) < len(zoom_urls) ):
        wd = int(sys.argv[1])
    elif(sys.argv[1] in dias):
        wd = dias.index(sys.argv[1])
    else:
        print("\nSin parámetros es la clase de hoy\n")
        print("Uso del parámetro:\n")
        for i in range(len(zoom_urls)):
            print(i, dias[i], ":", zoom_urls[i][0])
        exit()
else:
    # Monday is 0 and Sunday is 6.
    wd = datetime.datetime.today().weekday()

zoom_nro = zoom_urls[wd][1]
zoom_url = "zoommtg://zoom.us/join?confno=" + zoom_nro
zoom_pass = zoom_urls[wd][2]

print("\n", zoom_urls[wd][0], "\n")
print("url:", zoom_url, "copiada en el portapapeles")
clipboard.copy(zoom_url)
# para que ditto lo tome necesita un respiro ;) dicen 500ms
time.sleep(.8)
print("pass:", zoom_pass, "copiada en el portapapeles")
clipboard.copy(zoom_pass)

# ejecuta zoom, y como parametro va todo eso y el numero de reunion :)
# subprocess.run() espera a que termine el proceso....
# pero no quiero ;p así que uso Popen
subprocess.Popen([os.getenv('APPDATA') + "\\Zoom\\bin\\Zoom.exe", "--url=zoommtg://zoom.us/join?confno=" + zoom_nro])

# pega el pass solito al aparecer la ventana de zoom! OMG! Genial!!
# para poder pararlo con Ctrl+C
try:
    while 'Introducir' not in win32gui.GetWindowText(win32gui.GetForegroundWindow()):
        time.sleep(0.2)
    
    pyautogui.typewrite(zoom_pass + '\n')
except KeyboardInterrupt:
    print("Bye!")


# Enjoy :)