from selenium import webdriver
from selenium.webdriver.common.by import By
import time

baseUrl = ""
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseUrl)
driver.implicitly_wait(3)
partialText = ""
textToSelect = ""

textElement = driver.find_element(By.ID, "")
textElement.send_keys(partialText)

ulElement = driver.find_element(By.ID, "")
inner_html = ulElement.get_attribute("")
# print(inner_html)

liElements = ulElement.find_elements(By.TAG_NAME, "")
time.sleep(2)

for element in liElements:
    if textToSelect in element.text:
        element.click()
        break

time.sleep(4)

driver.quit()
