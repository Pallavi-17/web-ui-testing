import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def browser():
  driver = webdriver.Chrome(executable_path="D:\\drivers\\chromedriver.exe")
  driver.implicitly_wait(20)
  yield driver
  driver.quit()


def test_basic_duckduckgo_search(browser):
    URL = 'https://www.duckduckgo.com'
    PHRASE = 'panda'
    browser.get(URL)
    search_input = browser.find_element_by_id('search_form_input_homepage')
    # The RETURN key at the end submits the search.
    search_input.send_keys(PHRASE + Keys.RETURN)