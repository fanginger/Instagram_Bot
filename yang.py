"""
Created on : 2021/1/25

author : Ginger
"""

import selenium.common.exceptions
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import random

exe_path = ''
username = ''
password = ''
url = 'https://www.instagram.com/'
back_pass = ''
tags=['afufu_']


def path():
    global chrome
    chrome = webdriver.Chrome(ChromeDriverManager().install())


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

def work():
    for tag in tags:
          chrome.get("https://www.instagram.com/explore/tags/" + tag) 
          time.sleep(random.randint(2,5))
          work_opt('follow',2)


def work_opt(opt,post_num=None):
     chrome.find_elements_by_class_name('_9AhH0')[0].click()

     if opt == 'newest':
          pass 
     else:
          time_sleep(3,5)
          chrome.find_elements_by_class_name('e1e1d')[0].click() #帳號
          time_sleep(1,5)
          chrome.find_elements_by_class_name('-nal3')[2].click() #帳號的追縱者
          time_sleep(2,5) 
          chrome.find_elements_by_class_name('FPmhX.notranslate._0imsa')[0].click() #第一位追縱者
          time_sleep(2,5)
          chrome.find_elements_by_class_name('_9AhH0')[0].click() #第一篇文章

     for i in range(post_num):
          click_like()
          time_sleep(2,4)
          chrome.find_elements_by_class_name('coreSpriteRightPaginationArrow')[0].click() #點下一篇         


def click_like():
     time_sleep(3,7)
     if len(chrome.find_elements_by_xpath('//*[@aria-label="Unlike"]')) != 0 or len(chrome.find_elements_by_xpath('//*[@aria-label="收回讚"]')) != 0:
          print('already')
     else:
          time.sleep(random.randint(1,3))
          chrome.find_element_by_xpath('//*[@aria-label="讚"]').click()
          print('completed')


def time_sleep(min,max):
     time.sleep(random.randint(min,max))


path()
time.sleep(1)
url_name(url)

login(username, password)

# back_click_fun()

work()

chrome.close()
