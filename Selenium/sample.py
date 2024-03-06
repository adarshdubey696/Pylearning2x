# import time
#
# from selenium import webdriver
# webdriver.Chrome()
# time.sleep(10)
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")

# Uolo site
# driver.get("https://manage-stage.uolo.co")
driver.find_element("username").send_keys("Username : Admin")
driver.find_element("password").send_keys("Password : admin123")
driver.find_element("submit").submit()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login is passed")
else:
    print("Login is failed")

# driver.close()

time.sleep(10)
