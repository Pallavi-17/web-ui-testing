import pytest
import time
from selenium import webdriver
from  selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
  driver = webdriver.Chrome(executable_path="D:\\drivers\\chromedriver.exe")
  driver.implicitly_wait(20)
  yield driver
  driver.quit()


def test_basic_google_search(browser):
    URL = 'https://www.google.com'
    PHRASE = 'Naveen automationlabs'
    browser.get(URL)
    search_input = browser.find_element(By.NAME, 'q')
    search_input.send_keys("Naveen automationlabs")
    print(browser.title)
    optionList = browser.find_elements(By.XPATH,"//ul[@class='erkvQe']//li")
    print(len(optionList))
    assert len(optionList) > 0

    for ele in optionList:
        print(ele.text)


    #assert ele.text == 'Naveen automationlabs'

    assert search_input.get_attribute('value') == PHRASE

    assert browser.title == 'Google'
    time.sleep(6)
    browser.quit()
    #search_input = browser.find_element_by_id('search_form_input_homepage')
    # The RETURN key at the end submits the search.
    #search_input.send_keys(PHRASE + Keys.RETURN)