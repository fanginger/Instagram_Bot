"""
Created on : 2021/1/25

author : Ginger
"""

import selenium.common.exceptions
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random

exe_path = ''
username = ''
password = ''
url = 'https://www.instagram.com/'
back_pass = ''
tags=['dogsofinstagram','dogofinsta','thedodo','cutedog','mydog','farmlife']



def path():
    global chrome
    chrome = webdriver.Chrome(executable_path=exe_path)


def url_name(url):
    # the web page opens up
    chrome.get(url)
    time.sleep(4)


def login(username, your_password):
    usern = chrome.find_element_by_name("username")

    # sends the entered username
    usern.send_keys(username)

    # finds the password box
    passw = chrome.find_element_by_name("password")

    # sends the entered password
    passw.send_keys(your_password)
    passw.send_keys(Keys.RETURN)
    time.sleep(6)
    notn = chrome.find_element_by_class_name("sqdOP")  # dont save info button
    notn.click()  # click don't save button

    time.sleep(5)

def back_click_fun():
     back = chrome.find_element_by_name("verificationCode")
     time.sleep(3)
     back.send_keys(back_pass)

     time.sleep(5)
     back_click = chrome.find_element_by_class_name("sqdOP")
     back_click.click()
     time.sleep(5)

def click_like():
    for tag in tags:
          chrome.get("https://www.instagram.com/explore/tags/" + tag) 
          time.sleep(random.randint(2,5))
          chrome.find_elements_by_class_name('_9AhH0')[9].click() #點選圖片(選擇最新發的)
          for i in range(random.randint(40,50)):
               if i % 10 == 1:
                    time.sleep(random.randint(5,20))
                    if len(chrome.find_elements_by_xpath('//*[@aria-label="Unlike"]')) != 0 or len(chrome.find_elements_by_xpath('//*[@aria-label="收回讚"]')) != 0:
                         print('按過了')
                    else:
                         time.sleep(random.randint(1,3))
                         chrome.find_element_by_xpath('//*[@aria-label="讚"]').click()
                         print('已按完')
               chrome.find_elements_by_class_name('coreSpriteRightPaginationArrow')[0].click()
               time.sleep(random.randint(1,5))
          print(tag +'按完了')
          time.sleep(random.randint(7,15)) 

path()
time.sleep(1)
url_name(url)

login(username, password)

back_click_fun()

click_like()

chrome.close()
