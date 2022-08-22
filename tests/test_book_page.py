"""Тестируем книги с главной страницы. 4 теста."""


from pages.labirint_locators import MainPage



"""Тестируем, что выбранная книга добалена в корзину"""


def test_add_best_book_to_cart(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()

    assert page.successfuly_odered

"""Тестируем, что выбранная книга добалена в отложенные"""

def test_add_best_book_to_deferred(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.add_to_deferred.click()
    page.deferred.click()

    assert page.successfuly_deferred

"""Тестируем, что выбранная книга добалена к сравнению"""

def test_add_best_book_to_comparison(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.compare.click()

    assert page.successfuly_compared


"""Тестируем сравнение книг"""


def test_compare_books(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.compare.click()
    page.logo.click()
    page.best_sale.click()
    page.random_book_1.click()
    page.compare.click()
    page.compare_books.click()

    assert page.get_current_url() == 'https://www.labirint.ru/compare/'
