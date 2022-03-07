from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def testListOfElements(self):
        baseUrl = ""
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(
            By.XPATH, "")
        size = len(radioButtonsList)
        print("Size of the list: " + str(size))

        for radioButton in radioButtonsList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)

ff = WorkingWithElementsList()
ff.testListOfElements()
