from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import element_to_be_selected


#Interacting with the page
#<input type="text" name="passwd" id="passwd-id" />
# element = driver.find_element(By.ID, "passwd-id")
# element = driver.find_element(By.NAME, "passwd")
# element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
# element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")


driver = webdriver.Chrome()
driver.get("http://www.google.com")

element = driver.find_element(By.NAME, "kumi")
element.send_keys("some text")
element.send_keys(" and some", Keys.ARROW_DOWN)
element.clear()
