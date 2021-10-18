import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://cuenta.elcorteingles.es/external/registro/?back_to=/")
time.sleep(5)

usr = driver.find_element_by_name("login")
usr.send_keys("wigid99193@wawue.com")
psw = driver.find_element_by_name("password")
psw.send_keys('abcd1234')
psw_conf = driver.find_element_by_name("password-confirmation")
psw_conf.send_keys('abcd1234')
name = driver.find_element_by_name("name")
name.send_keys("as")
name2 = driver.find_element_by_name("surname1")
name2.send_keys("as")
driver.find_element_by_id("tos").click()
driver.find_element_by_xpath("//*[@id='modal-content']/div/div/div/div/div[2]/button").click()
driver.find_element_by_id("signup-step-1").click()