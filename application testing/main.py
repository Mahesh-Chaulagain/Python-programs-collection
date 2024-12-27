# script that loads python.org website perform a search and validates result by comparing the resulting page against 
# 'no results found' message

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# set the driver to use webbrowser
driver = webdriver.Chrome()
# load the target website
driver.get('https://www.python.org')
# validate the page loaded by comparing the page title
assert "Python" in driver.title
# find the search input element by name
elem = driver.find_element(By.NAME, "q")
# Empty it 
elem.clear()
# type 'pycon'
elem.send_keys('pycon')
# press an enter to trigger the search form 
elem.send_keys(Keys.RETURN)
# validate that the test 'No results found.' is not present in the page
assert 'No results found.' not in driver.page_source
# close the browser
driver.close()