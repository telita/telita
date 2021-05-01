from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver")
driver.get("https://www.logitravel.com")
a = driver.find_element_by_class_name("searcher searcher--flight-hotel is-visible searcher--default is-load")
a.sen
origen = driver.find_element_by_class_name("input__input tt-input")
origen.send_keys("PMI")
time.sleep(5)
driver.close()
