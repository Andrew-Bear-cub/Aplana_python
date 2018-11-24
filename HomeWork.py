import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Класс теста
class HomeWork(unittest.TestCase):

    # Эта функция выполняется перед каждым тестом
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://google.com/ncr')

    # Функция теста
    def test_homeWork(self):

        # Нашли строку поиска на странице
        search_field = self.driver.find_element_by_name('q')

        # Ввели туда selenide
        search_field.send_keys('selenide')
        search_field.send_keys(Keys.RETURN)

        # по икспасу нашел ссылку на первый результат поиска и сделал предположение, что там содержится selenide.org
        search_result = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div/div[1]/a/div/cite')
        assert 'selenide.org' in search_result.get_attribute('innerHTML')

        # по икспасу нашел и перешел на поиск картинок
        image_search = self.driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a')
        image_search.click()

        # по икспасу нашел ссылку на первый результат поиска и сделал предположение, что там содержится selenide.org
        image_search_result = self.driver.find_element_by_xpath('//*[@id="rg_s"]/div[1]/a[2]/div[2]')
        assert 'selenide.org' in image_search_result.get_attribute('innerHTML')

        # Вернулся на вкладку со всеми результатми поиска
        all_search = self.driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[1]/a')
        all_search.click()

        # по икспасу нашел ссылку на первый результат поиска и сделал предположение, что там содержится selenide.org
        search_result = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div/div[1]/a/div/cite')
        assert 'selenide.org' in search_result.get_attribute('innerHTML')

    # Эта Функция выполняется после кажого теста
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
