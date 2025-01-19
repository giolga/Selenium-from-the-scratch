from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import element_to_be_selected

driver = webdriver.Chrome()

driver.implicitly_wait(15)

driver.get("https://www.tutorialspoint.com/selenium/practice/buttons.php")

button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()

txt_output = driver.find_element(By.ID, "welcomeDiv")
print(f"Text obtained: {txt_output.text}")

driver.quit()


driver = webdriver.Chrome()
driver.get("https://www.python.org/")
assert 'Welcome to Python.org' in driver.title

element = driver.find_element(By.NAME, 'q')
element.clear()
element.send_keys('pycon')
element.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

print('chama!')
driver.quit()


