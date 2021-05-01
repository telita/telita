from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
driver.get("https://opensource-demo.orangehrmlive.com/")
username = driver.find_element_by_id("txtUsername")
password = driver.find_element_by_id("txtPassword")
username.send_keys("Admin")
password.send_keys("admin123")
login = driver.find_element_by_id("btnLogin")
login.click()
time.sleep(5)
driver.close()
