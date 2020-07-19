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

def test_window_handle(browser):
      URL = 'http://demo.automationtesting.in/Windows.html/'
      browser.get(URL)
      we = browser.find_element(By.LINK_TEXT, 'Open New Tabbed Windows')
      we.click()
      print(browser.current_window_handle)
      handles = browser.window_handles

      for handle in handles:
          browser.switch_to.window(handle)
          print(browser.title)




