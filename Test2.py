from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from selenium.webdriver.support.ui import Select


#Interacting with the page
#<input type="text" name="passwd" id="passwd-id" />
# element = driver.find_element(By.ID, "passwd-id")
# element = driver.find_element(By.NAME, "passwd")
# element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
# element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")


driver = webdriver.Chrome()
driver.get("http://www.google.com")

# element = driver.find_element(By.NAME, "kumi")
# element.send_keys("some text")
# element.send_keys(" and some", Keys.ARROW_DOWN)
# element.clear()

element = driver.find_element(By.XPATH, "//select[@name='name']")
all_options = element.find_elements(By.TAG_NAME, "option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()

select = Select(driver.find_element(By.NAME, 'ExampleName'))
select.select_by_index(2)
select.select_by_value("thisExampleValue")
select.select_by_visible_text("ExampleText")

select = Select(driver.find_element(By.ID, 'id'))
select.deselect_all() #deselects everything

options = select.options #get all Available options!

