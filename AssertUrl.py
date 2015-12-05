# coding=UTF-8
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait

import unittest

class AssertUrlTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://2gis.ru/"
    
    def test_assertUrl(self):
        driver = self.driver
        driver.get(self.base_url + "/novosibirsk")
        getAddress = driver.find_element_by_name('search[query]')
        getAddress.send_keys(u'ШТРИХ-М Новосибирск')
        # click searchBar
        driver.find_element_by_css_selector('button.searchBar__submit._directory').click()
        # click company name
        driver.find_element_by_css_selector('#module-1-12-1-1-1-3 > div > header > a').click()
        # assert current_url
        self.assertEquals(driver.current_url, "http://2gis.ru/novosibirsk/search/%D0%A8%D0%A2%D0%A0%D0%98%D0%A5-%D0%9C%20%D0%9D%D0%BE%D0%B2%D0%BE%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA/firm/141265769449200/tab/firms/zoom/11")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()