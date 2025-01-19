from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import element_to_be_selected

#Filling in forms

driver = webdriver.Chrome()
driver.get("http://www.google.com")