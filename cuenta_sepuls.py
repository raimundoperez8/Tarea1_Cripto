import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://sepuls.cl/customer/registration")
time.sleep(5)

usr = driver.find_element_by_id("customer_email")
usr.send_keys("besov88676@specialistblog.com")
phone = driver.find_element_by_id("customer_phone")
phone.send_keys("123456789")
rut = driver.find_element_by_id("customer_contact_rut")
rut.send_keys("1-9")
psw = driver.find_element_by_id("customer_password")
psw.send_keys("1Q2W3E4R5t")
pswcon = driver.find_element_by_id("customer_password_confirmation")
pswcon.send_keys("1Q2W3E4R5t")

clk = driver.find_element_by_xpath("//*[@id='register_customer']").click()
