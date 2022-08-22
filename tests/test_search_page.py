"""Тестируем поиск по тексту с главной страницы. 7 тестов."""

from pages.labirint_locators import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""Тестируем поиск с корректным названием"""


def test_successful_search(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Гнев всемогущий')
    page.search_btn.click()

    assert page.successful_search

"""Тестируем поиск с названием лотиницей"""


def test_successful_latinica(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Gnev vsemogushchiy')
    page.search_btn.click()

    assert page.successful_search

"""Тестируем поиск по цифрам"""


def test_successful_numbers(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('123456')
    page.search_btn.click()

    assert page.successful_search


"""Тестируем поиск по пробелам"""


def test_not_successful_blanc(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('           ')
    page.search_btn.click()

    assert page.not_successful_search


"""Тестируем поиск по случайным символам"""


def test_not_successful_search_random(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('!@#$%^&*()')
    page.search_btn.click()

    assert page.not_successful_search


"""Тестируем поиск по тексту с главной страницы с применением фильтров - в наличии"""


def test_only_available(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Я учусь кодить')
    page.search_btn.click()
    page.all_filers.click()
    page.reset_all_filers.click()
    page.available.click()
    page.show_all_found.click()
    element = WebDriverWait(web_browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//*[@class="btn buy-link btn-primary"]'))
    )

    assert element


"""Тестируем поиск по тексту с главной страницы с применением фильтров - нет вналичии"""


def test_only_not_available(web_browser):
    page = MainPage(web_browser)
    page.search.send_keys('Я учусь кодить')
    page.search_btn.click()
    page.all_filers.click()
    page.reset_all_filers.click()
    page.not_available.click()
    page.show_all_found.click()

    element = WebDriverWait(web_browser, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//span[text()="Нет в продаже"]'))
    )

    assert element
