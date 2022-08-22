import os
from pages.base import WebPage
from pages.elementes import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    """Параметризация"""
    parametr_page=WebElement(xpath=input)



    """Авторизация"""

    login_field = WebElement(xpath='//*[@class="full-input__input formvalidate-error"]')
    enter = WebElement(xpath='//*[@id="g-recap-0-btn"]')
    automatic_closing = WebElement(xpath='//*[@id="auth-success-login"]/input[2]')
    auth_error = WebElement(xpath='//a[contains(text(),"Введенного кода не существует")]')
    auth_error_2 = WebElement(xpath='//span[contains(text(),"Нельзя использовать символ «{N}»")]')


    """Результаты поиска"""

    search = WebElement(id='search-field')
    search_btn = WebElement(xpath='//button[@type="submit"]')
    successful_search = WebElement(xpath='//span[contains(text(),"Все, что мы нашли в Лабиринте по запросу")]')
    not_successful_search = WebElement(xpath='//h1[contains(text(),"Мы ничего не нашли по вашему запросу! Что '
                                             'делать?")]')
    all_filers = WebElement(xpath='//span[contains(text(), "ВСЕ ФИЛЬТРЫ") and @class="navisort-item__content"]')
    reset_all_filers = WebElement(xpath='//*[@id="rubric-tab"]/div[2]/div[1]/div/div[2]/div/span[3]')
    available = WebElement(xpath='//*[@id="section-search-form"]/div[2]/div[2]/div[1]/label[1]/span[2]')
    not_available = WebElement(xpath='//*[@id="section-search-form"]/div[2]/div[2]/div[4]/label[1]/span[2]')
    show_all_found = WebElement(xpath='//input[@class="show-goods__button"]')

    """Книги"""

    best_sale = WebElement(xpath='//a[@href="/best/sale/"]')
    random_book = WebElement(xpath='//*[@class="b-productblock-e-cover"]')
    random_book_1 = WebElement(xpath='//*[@class="relative product-cover__relative"]')
    buy_book = WebElement(xpath='//*[@class="btn btn-small btn-primary btn-buy"]')
    successfuly_odered = WebElement(xpath='//span[contains(text(),"Ваш заказ")]')
    add_to_deferred = WebElement(xpath='//a[@class="fave"]')
    successfuly_deferred = WebElement(xpath='//a[@title="Выделить все отложенные товары"]')
    compare = WebElement(xpath='//span[contains(text(),"+ к сравнению")]')
    successfuly_compared = WebElement(xpath='//*[@class="compare big-compare done"]')
    compare_books = WebElement(xpath='//a[@href="/compare/"]')

    """Корзина"""

    plus_one_more = WebElement(xpath='//span[@class="btn btn - increase btn-increase-cart"]')
    #plus_one_more = WebElement(xpath='//span[@class="btn btn-small btn-primary plusone"]')
    remove_from_cart = WebElement(xpath='//span[@class="btn btn-lessen btn-lessen-cart"]')
    two_books_in_cart = WebElement(xpath='//input[Compare(test()), "2") and @class="quantity"]')
    empty_cart = WebElement(xpath='//span[contains(text(),"Ваша корзина пуста. Почему?"]')
    btn_ok_close = WebElement(xpath='//span[@class="fright btn btn-primary btn-middle"]')
