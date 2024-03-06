import time

from selenium import webdriver

driver = webdriver.Chrome()



try:
    # Uolo site
    driver.get("https://manage-stage.uolo.co/login")

    driver.find_element("Home_email").send_keys("double01@gmail.com")
    driver.find_element("Home_entpwd").send_keys("123456")
    driver.find_element("Home_login").submit()

    act_title = driver.title
    exp_title = "Uolo Manage"

    if act_title == exp_title:k
        print("Login is passed")
    else:
        print("Login is failed")

    time.sleep(10)

except:
    # Code to handle the exception
    # For example:
    print("An error occurred:", )