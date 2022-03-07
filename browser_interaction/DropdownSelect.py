from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class DropdownSelect():

    def test(self):
        baseUrl = ""
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("")
        sel = Select(element)

        sel.select_by_value("")
        print("Select by value")
        time.sleep(2)

        sel.select_by_index("2")
        print("Select by index")
        time.sleep(2)

        sel.select_by_visible_text("")
        print("Select by visible text")
        time.sleep(2)

        sel.select_by_index(2)
        print("Select by index")


ff = DropdownSelect()
ff.test()
