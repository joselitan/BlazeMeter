from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.maximize_window()

driver.get(" ")

