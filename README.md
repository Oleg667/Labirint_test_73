Проект по курсу Тестировщик-автоматизатор на Python (QAP) с использованием PyTest и Selenium интернет-магазина Labirint.ru.
Для запуска тестов необходимо предварительно установить следующие библиотеки (pip install):

pytest;
pytest-selenium;
selenium;
termcolor;
allure-python-commons;

Необходимо указать свой путь для драйвера, в моем случае он лежит в папке C:\ChromeDriveSelenium\chromedriver.exe

Для запуска всех тестов  необходимо ввести команду: pytest -v --driver Chrome --driver-path C:\ChromeDriveSelenium\chromedriver.exe

ПАПКА tests

Тестируемые сценарии:

tests_test_auth_page.py - Тестируем возможность входа в личный кабинет. 4 теста. 
Для запуска теста вводим команду:           pytest -v --driver Chrome --driver-path C:\ChromeDriveSelenium\chromedriver.exe tests\test_auth_page.py

test_book_page.py - Тестируем книги с главной страницы. 4 теста. 
Для запуска теста вводим команду:           pytest -v --driver Chrome --driver-path C:\ChromeDriveSelenium\chromedriver.exe tests\test_book_page.py

test_home_page.py - Тестируем главную страницу 50 тестов. 
Для запуска теста вводим команду:           pytest -v --driver Chrome --driver-path C:\ChromeDriveSelenium\chromedriver.exe tests\test_labirint.py

test_search_page.py - Тестируем поиск по тексту с главной страницы. 7 тестов. 
Для запуска теста вводим команду:           pytest -v --driver Chrome --driver-path C:\ChromeDriveSelenium\chromedriver.exe tests\test_search_page.py

test_cart_page.py - Тестируем корзину с книгами. 3 теста. 
Для запуска теста вводим команду:           pytest -v --driver Chrome --driver-path C:\ChromeDriveSelenium\chromedriver.exe tests\test_cart_page.py



ПАПКА Test_par
test_parametr_home_page.py - параметризованный обход кнопок в шапке главной страницы сайта. 18 тестов
Для запуска теста вводим команду:           pytest -v --driver Chrome --driver-path C:\ChromeDriveSelenium\chromedriver.exe tests\ttest_parametr_home_page.py

test_parametr_office.py - параметризованный обход кнопок в разделе Канцтовары. 10 тестов
Для запуска теста вводим команду:           pytest -v --driver Chrome --driver-path C:\ChromeDriveSelenium\chromedriver.exe tests\test_parametr_office.py

