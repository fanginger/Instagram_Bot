# Selenium_ig按愛心

## Goal

Instagram bot using Selenium 

我按愛心，希望增加別人可能會按回來的機率

### Technologies used

- Python
- Selenium

### Code

### 🖊️ 設定webdriver、輸入帳號密碼

這邊登入自己帳號密碼、在上面有寫自己的帳密。而這邊back_click_fun 就是使用備用密碼雙重認證得進去得。

必須輸入您的帳號密碼，以方便自動登入。tags則是輸入想要到哪個tag按讚，因此這些tag通常要與品牌最有相關。

```python
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
```

### 🖊️  按愛心

這邊跑每一個設定的tag 網址，然後按愛心是最新的

chrome.find_elements_by_class_name('_9AhH0')[9].click() 寫在這

```python
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
                         try:
                              chrome.find_element_by_xpath('//*[@aria-label="讚"]').click()
                              print('已按完')
         
               chrome.find_elements_by_class_name('coreSpriteRightPaginationArrow')[0].click()
               time.sleep(random.randint(1,5))
          print(tag +'按完了')
          time.sleep(random.randint(7,15))
```

### REL.

[小編神器，IG愛心大放送，selenium在IG上的實做](https://medium.com/@ivanyang0606/%E5%B0%8F%E7%B7%A8%E7%A5%9E%E5%99%A8-ig%E6%84%9B%E5%BF%83%E5%A4%A7%E6%94%BE%E9%80%81-selenium%E5%9C%A8ig%E4%B8%8A%E7%9A%84%E5%AF%A6%E5%81%9A-c891d95526bd)

[Like instagram pictures using Selenium | Python - GeeksforGeeks](https://www.geeksforgeeks.org/like-instagram-pictures-using-selenium-python/)