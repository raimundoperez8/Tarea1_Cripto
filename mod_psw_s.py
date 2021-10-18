import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://sepuls.cl/customer/login#")
time.sleep(5)

usr = driver.find_element_by_id("customer_email")
usr.send_keys("besov88676@specialistblog.com")
psw = driver.find_element_by_id("customer_password")
psw.send_keys("1Q2W3E4R5t")

clk = driver.find_element_by_xpath("//*[@id='submit_login']").click()
time.sleep(5)
clk1 = driver.find_element_by_xpath("/html/body/b/b/div[3]/div/div[1]/div[1]/div/div/a/i").click()

psw = driver.find_element_by_id("customer_password")
psw.send_keys("1Q2W3E4R5t6y")
pswcon = driver.find_element_by_id("customer_password_confirmation")
pswcon.send_keys("1Q2W3E4R5t6y")

clk2 = driver.find_element_by_xpath("//*[@id='register_customer']").click()