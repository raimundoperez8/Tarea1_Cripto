import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://sepuls.cl/customer/login")
time.sleep(5)

clk = driver.find_element_by_xpath("//*[@id='reset_password']").click()

usr = driver.find_element_by_id("customer_email")
usr.send_keys("besov88676@specialistblog.com")

clk1 = driver.find_element_by_xpath("//*[@id='submit_login']").click()

