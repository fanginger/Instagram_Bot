from bs4 import BeautifulSoup as bs
import selenium.common.exceptions
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("enter username")
username = 'afufu_dongua'
# username = 'ginger_94090'

print("enter password")
password = 'k148426'
# password = 'gingerfan'

print("enter the url")
url = 'https://www.instagram.com/'


def path():
    global chrome
    print("enter the driver path")
    exe_path = '/Users/ginger/Desktop/chromedriver'

    # starts a new chrome session
    chrome = webdriver.Chrome(executable_path=exe_path)


def url_name(url):
    # the web page opens up
    chrome.get(url)
    time.sleep(4)


def login(username, your_password):

    # finds the login button
#     log_but = chrome.find_element_by_class_name("L3NKy")
#     time.sleep(2)

    # clicks the login button
    # log_but.click()
    # time.sleep(4)

    # finds the username box
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
    print('2')

def back_click_fun():
     print('1')
     back = chrome.find_element_by_name("verificationCode")
     time.sleep(3)
     back_pass = '80359274'
     back.send_keys(back_pass)

     time.sleep(5)
     back_click = chrome.find_element_by_class_name("sqdOP")
     back_click.click()
     print('here')
     time.sleep(5)


tags=['dog','dogofinsta']

import random
def first_picture():

    for tag in tags:
          chrome.get("https://www.instagram.com/explore/tags/" + tag) #切換到該tag
          time.sleep(random.randint(2,5))
          chrome.find_elements_by_class_name('_9AhH0')[9].click() #點選圖片(選擇最新發的)
          for i in range(random.randint(40,50)):
               # if i % 10 == 1:
                    # time.sleep(random.randint(5,20))
                    # 檢查有沒有按過讚
               if len(chrome.find_elements_by_xpath('//*[@aria-label="Unlike"]')) != 0 or len(chrome.find_elements_by_xpath('//*[@aria-label="收回讚"]')) != 0:
                    print('按過了')
               else:
                    time.sleep(random.randint(1,3))
                    try:
                         chrome.find_element_by_xpath('//*[@aria-label="讚"]').click()
                         print('已按完')
                    except:
                         print('圖片沒跑出來，直接下一頁')
               chrome.find_elements_by_class_name('coreSpriteRightPaginationArrow')[0].click()
               time.sleep(random.randint(1,5))
          print(tag +'按完了')
          time.sleep(random.randint(7,15)) # 按完一個tag稍微休息一下，盡量模仿真人
path()
time.sleep(1)

url_name(url)

login(username, password)

back_click_fun()

first_picture()
# like_pic()

# continue_liking()
chrome.close()
