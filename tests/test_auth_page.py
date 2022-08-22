"""Тестируем возможность входа  в личный кабинет с корректным и некорректным логином (код скидки). 4 теста."""

from pages.labirint_locators import MainPage

"""Вход с корретными данными"""


def test_valid_login_auth_page(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("1208-41C9-80DB")
    page.enter.click()
    page.automatic_closing.click()

    assert page.get_current_url() == 'https://www.labirint.ru/'


"""Вход с некорретными данными"""


def test_invalid_login_auth_page(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("12F8-41C9-80DB")
    page.enter.click()

    assert page.auth_error


"""Вход с пробелом"""


def test_blanc_login_auth_page(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("      ")

    assert page.auth_error_2


"""Вход по электронной почте"""


def test_email_login_auth_page(web_browser):
    page = MainPage(web_browser)
    page.my_labirint.click()
    page.login_field.send_keys("len8272@gmail.com")
    page.enter.click()

    assert page.login_field
