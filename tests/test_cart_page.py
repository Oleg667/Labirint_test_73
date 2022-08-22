"""Тестируем корзину с книгами. 3 теста."""


from pages.labirint_locators import MainPage


"""Тестируем, что книга добалена в корзину"""


def test_add_book_to_cart(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    #page.btn_ok_close.click()

    assert page.successfuly_odered


"""Добавляем книгу  и увеличиваем количество книг на 1 (2 книги в коризне)"""


def test_make_more_books_in_cart(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    page.btn_ok_close.click()
    page.plus_one_more.click()



    assert page.two_books_in_cart


"""Добавляем и удаляем книгу (пустая корзина)"""


def test_remove_book_from_cart(web_browser):
    page = MainPage(web_browser)
    page.best_sale.click()
    page.random_book.click()
    page.buy_book.click()
    page.cart.click()
    #page.btn_ok_close.click()
    page.remove_from_cart.click()

    assert page.empty_cart
