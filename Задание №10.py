import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Search(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome('chromedriver.exe')
        self.drv.get('http://google.com/ncr')

    def test_search(self):
        assert 'Google' in self.drv.title
        elm = self.drv.find_element_by_name('q')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)
        time.sleep(1)
        assert 'No results found' not in self.drv.page_source
        results = self.drv.find_element_by_id('search')
        links = results.find_elements_by_tag_name("a")
        href = links[0].get_attribute("href")
        if href == 'https://selenide.org/':
            print(f'Первый результат поиска по всему Интернету: {href}, как и ожидалось.')
        else:
            print(f'Первый результат поиска по всему Интернету: {href}, чего мы не ожидали!')
        top_menu_items = self.drv.find_elements_by_class_name('hdtb-mitem')
        for item in top_menu_items:
            if item.text == "Images" or item.text == "Картинки":
                item.click()
                time.sleep(.5)
                break
        assert 'Google' in self.drv.title
        results = self.drv.find_elements_by_class_name('fxgdke')
        if results[0].text == 'selenide.org':
            print(f'Первый результат поиска изображений неким образом связан с сайтом selenide.org, как и ожидалось.')
        else:
            print(f'Первый результат поиска изображений неким образом связан с сайтом: {results[0].text}, чего мы не ожидали!')
        top_menu_items = self.drv.find_elements_by_class_name('NZmxZe')
        for item in top_menu_items:
            if item.text == "All" or item.text == "Все":
                item.click()
                time.sleep(.5)
                break
        assert 'Google' in self.drv.title
        results = self.drv.find_element_by_id('search')
        links = results.find_elements_by_tag_name("a")
        href = links[0].get_attribute("href")
        if href == 'https://selenide.org/':
            print(f'Первый результат поиска по всему Интернету: {href}, как и ожидалось.')
        else:
            print(f'Первый результат поиска по всему Интернету: {href}, чего мы не ожидали!')

    def tearDown(self):
        #time.sleep(100)
        self.drv.close()

if __name__ == '__main__':
    unittest.main()