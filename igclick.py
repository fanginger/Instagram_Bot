"""
Created on : 2021/1/25

author : Ginger
"""

import selenium.common.exceptions
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import random

exe_path = '/Users/ginger/Desktop/chromedriver'
username = 'afufu_dongua'
# username = 'ginger_94090'
password = 'k148426'
# password = 'ginger fan'
url = 'https://www.instagram.com/'
back_pass = '69412873'
tags=['dogsofinstagram','cutedog','mydog','doglife','dogoftheday','doglover']

# TODO farmlife 標籤都無法跑圖片

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
          time.sleep(random.randint(5,10))
          for i in range(50):
               if random.randint(1,2) == 1:
                    if len(chrome.find_elements_by_xpath('//*[@aria-label="Unlike"]')) != 0 or len(chrome.find_elements_by_xpath('//*[@aria-label="收回讚"]')) != 0:
                         print('按過了')
                    else:
                         try:
                              chrome.find_element_by_xpath('//*[@aria-label="讚"]').click()
                              print('已按完')
                         except:
                              print('圖片沒跑出來，直接下一頁')

               chrome.find_elements_by_class_name('coreSpriteRightPaginationArrow')[0].click()
               time.sleep(random.randint(1,5))
          print(tag +'按完了')
          time.sleep(random.randint(7,15)) 
# def tell_priviate():
#      user_type = chrome.find_element_by_xpath("/html/body/script[1]")
#      user_type_attr = user_type.get_attribute("innerHTML")
#      fun = lambda x : True if '"is_private":true' in x else False
#      if '"is_private":true' in user_type_attr:
#           return True
#      else:
#           return False


path()
time.sleep(1)
url_name(url)

login(username, password)

back_click_fun()

click_like()

chrome.close()


