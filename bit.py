# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 02:09:38 2021

@author: Raza_Jutt
"""
import os
import subprocess
import time
from keyboard import press
from selenium import webdriver
import pyperclip
import pyautogui
import keyboard
m=893
n=12693
for i in range(0,15000):
    a = "https://www.blockchain.com/btc/blocks?page="+str(n)
    driver = webdriver.Chrome("C:/Users/Raza Jutt/Desktop/bit/chromedriver.exe")
    driver.get(a)
    press('tab')
    press('tab')
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    driver.quit()
    subprocess.Popen("notepad.exe")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 's')
    keyboard.write(str(m))
    press('enter')
    #os.close("notepad.exe")
    #time.sleep(1)
    print(m)
    print(n)
    print("done")
    m=m+1
    n=n-1


        