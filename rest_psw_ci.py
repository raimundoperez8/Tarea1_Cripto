import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://cuenta.elcorteingles.es/recuperar-contrasena/?back_to=&redirect_uri=")
time.sleep(5)

usr = driver.find_element_by_name("user")
usr.send_keys("wigid99193@wawue.com")
clk = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[2]/form/fieldset/div/div[2]/input").click()