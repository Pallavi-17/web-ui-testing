import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
  driver = webdriver.Chrome(executable_path="D:\\drivers\\chromedriver.exe")
  driver.implicitly_wait(20)
  yield driver
  driver.quit()


def select_values_dd(element, value):
    select = Select(element)
    select.select_by_visible_text(value)


def test_basic_dropDown_search(browser):
    URL = 'https://www.orangehrm.com/orangehrm-30-day-trial/'
    browser.get(URL)
    weIndustry = browser.find_element(By.ID, 'Form_submitForm_Industry')
    weCountry = browser.find_element(By.ID, 'Form_submitForm_Country')
    select_values_dd(weIndustry, 'Healthcare')
    select_values_dd(weCountry, 'Israel')
    weLastName = browser.find_element(By.ID, 'Form_submitForm_LastName')
    weEmail = browser.find_element(By.ID, 'Form_submitForm_Email')
    weLastName.send_keys('Singh')
    weEmail.send_keys('arSingh@gmail.com')
   # selectCountry.select_by_index(4)
    time.sleep(3)
    #print(selectCountry.is_multiple)
   # assert selectCountry.is_multiple == True
