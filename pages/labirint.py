import os
from pages.base import WebPage
from pages.elementes import WebElement
from pages.elementes import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    # поле основного поиска на главной странице
    search = WebElement(id='search-field')

    # кнопка основного поиска
    search_run_button = WebElement(
        xpath='//span[@class="b-header-b-search-e-srch-icon b-header-e-sprite-background"]')

    # названия книг в результатах поиска
    products_titles = ManyWebElements(
        xpath='//a[@class="product-title-link"]')

    # названия книг в результатах поиска тайный город
    products_titles1 = ManyWebElements(
        xpath='//td[@class="col-sm-4"]')

    # кноапка "вид-таблица" тайный город
    tabl_taun = ManyWebElements(
        xpath='//a[@class="radioitems-item view-table"]')


    # сообщение об ошибке поиска на главной странице
    msg_search_er = WebElement(
        xpath='//*[@id="search"]/div[1]/h1')

    # кнопка ТИП ТОВАРА
    product_type = WebElement(
        xpath='//span[@class="navisort-item__content" and contains(text(),"ТИП ТОВАРА")]')

    # в выпадающем списке - строка Бумажные книги
    paper_books = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Бумажные")]')

    # в выпадающем списке - строка Электронные книги
    electronic_books = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Электронные")]')

    # в выпадающем списке - строка Другие товары
    other_goods = WebElement(
        xpath='//label[@class="item-inner checkbox-ui  checked" and contains(text(),"Другие")]')

    # кнопка "Показать"
    show_button = WebElement(
        xpath='//input[@class="w100p show-goods__button" and @value="Показать"]')

    # тип товара в результатах поиска
    products_types = ManyWebElements(xpath='//span[@class="card-label__text card-label__text_inversed"]')

    # кнопка "Бумажные книги"
    without_paper_books_button = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Бумажные")]')

    # кнопка "Электронные книги"
    without_electronic_books_button = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Электронные")]')

    # кнопка "Прочие товары"
    without_others_products_button = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Прочие")]')

    # кнопка "В наличии"
    sort_products_by_type_in_stock_is = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"В наличии")]')

    # кнопка "Предзаказ"
    sort_products_by_type_order = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Предзаказ")]')

    # кнопка "Ожидаются"
    sort_products_by_type_waiting = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Ожидаются")]')

    # статус "Ожидается" в описании товара
    products_waiting = ManyWebElements(
        xpath='//a[@class="btn-not-avaliable"]')

    # часть описания товара, где расположена надпись "В корзину"
    products_in_stock = ManyWebElements(
        xpath='//div[@class="btn buy-link btn-primary"]')

    # кнопка "Нет в продаже"
    sort_products_by_type_out_of_stock = WebElement(
        xpath='//*[@class="filter-reset__content" and contains(text(),"Нет в продаже")]')

    # кнопка "Что почитать: выбор редакции"
    what_to_read_button = WebElement(
        xpath='//*[@id="right-inner"]/div[1]/div[1]/a')

    # названия книг на странице "Что почитать: выбор редакции"
    products_titles_large = ManyWebElements(
        xpath='//span[@class="product-title large-name"]')

    # заголовок страницы
    page_title = WebElement(xpath='//h1')

    # кнопка "Новинки"
    fair_button = WebElement(
        #xpath='//*[@id="bottom"]/div[1]/div[1]/a') Не работает
        xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]')


    # содержание раздела на открывшейся странице "Новинки"
    fair_content = WebElement(
        # xpath='//div[@class="t005__text t-text t-text_md"]')
        xpath='//div[@class="catalog-title"]')

    # кнопка "Акции"
    best_buy_button = WebElement(
        xpath='//*[@id="bottom"]/div[19]/div[1]/a[1]')

    #  на странице "Акция есть Лучшая покупка дня"
    products_pubhouse = ManyWebElements(
        xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[1]/div[1]/h2[1]/a[1]')

    # кнопка "Больше книг со скидками"
    discounts_button = WebElement(
        xpath='//*[@id="bottom"]/div[17]/div[1]/a[1]')

    # карточки книг в результатах поиска
    products_books = ManyWebElements(
        xpath='//div[@class="product need-watch watched" and @data-dir="books"]')

    # описание скидки на книгу в результатах поиска
    discounts_books = ManyWebElements(
        xpath='//a[contains(@class, "card-label_profit")]')

    # кнопка "Читатели выбирают сегодня"
    today_button = WebElement(
        xpath='//*[@id="bottom"]/div[6]/div[1]/a[1]')

    # кнопка "Книги" в основном меню header на черном фоне
    button_books = WebElement(
        xpath='/html/body/div[1]/div[5]/div[5]/div/div[1]/div[4]/div/div[1]/ul/li[1]/span/a')

    # кнопка "Молодежная литература" в выпадающем меню "Книги" основного меню в header
    button_youth_literature = WebElement(
        xpath='/html/body/div[1]/div[5]/div[5]/div/div[4]/div/ul/li[7]/a')

    # кнопка "Лабиринт. Сейчас"
    now_button = WebElement(
        xpath='//*[@id="bottom"]/div[8]/div[1]/a[1]')

    # активный пункт горизонтального меню, который соответсвует содержанию открывшейся страницы
    active_menu_item = WebElement(
        xpath='//a[@class="mm-link mm-link-big mm-link-big-m-sub active"]')

    # кнопка "Детский навигатор — что читать детям и с детьми"
    kids_button = WebElement(
        xpath='//*[@id="bottom"]/div[10]/div[1]/a[1]')

    # кнопка "Книги для школы"
    teenagers_button = WebElement(
        xpath='//*[@id="bottom"]/div[3]/div[1]/a[1]')

    # заголовок на открывшейся странице "Книги для школы"
    heading_on_the_page = WebElement(
        xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[1]/div[4]/h1[1]')

    # кнопка "Книжные лидеры продаж"
    leaders_button = WebElement(
        xpath='//*[@id="bottom"]/div[15]/div[1]/a[1]')

    # кнопка "Книги: новинки 2022"
    novelties_books_button = WebElement(
        xpath='//*[@id="bottom"]/div[17]/div[1]/a[1]')

    # заголовок на открывшейся странице "новинки 2022"
    novelties_title = WebElement(
        xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[1]/div[1]/h1[1]')

    # кнопка "Книжные обзоры и рецензии"
    reviews_button = WebElement(
        xpath='//*[@id="bottom"]/div[20]/div[1]/a[1]')

    # заголовок на открывшейся странице "Книжные обзоры и рецензии"
    heading_reviews = WebElement(
        xpath='//*[@id="newslist"]/div[1]/div[1]/div[1]')

    # кнопка "Доставка и оплата" в горизонтальном меню
    delivery_button = WebElement(
        xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]')

    # название раздела на странице "Доставка и оплата"
    section_title = WebElement(
        xpath='//*[@id="right-inner"]/div[1]/div[1]/div[1]/div[3]')

    # кнопка "Сертификаты" в горизонтальном меню
    certificates_button = WebElement(
        xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div[1]/ul[1]/li[2]/a[1]')

    # содержание раздела на открывшейся странице "Сертификаты"
    section_content = WebElement(
        xpath='//*[@id="newslist"]/div[1]/p[1]')

    # кнопка "Рейтинги" в горизонтальном меню
    ratings_button = WebElement(
        xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]')

    # кнопка "Новинки" в горизонтальном меню
    novelties_button = WebElement(
        xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div[1]/ul[1]/li[4]/a[1]')

    # кнопка "Скидки" в горизонтальном меню
    discounts_books_button = WebElement(
        xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div[1]/ul[1]/li[5]/a[1]')

    # кнопка "Контакты" в горизонтальном меню
    contacts_button = WebElement(
        xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div[1]/ul[1]/li[9]/a[1]')

    # кнопка "Поддержка" в горизонтальном меню
    support_button = WebElement(
        xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div[1]/ul[1]/li[10]/a[1]')

    # название раздела на странице "Поддержка"
    section_title_support = WebElement(
        xpath='//a[@class="support-all active"]')

    # кнопка "N пункт самовывоза" в горизонтальном меню
    export_button = WebElement(
        xpath='//*[@id="minwidth"]/div[5]/div[1]/div[2]/div[1]/ul[1]/li[11]/a[1]')

    # название раздела на странице "N пункт самовывоза"
    section_title_export = WebElement(
        xpath='//*[@id="js-tab-1"]/div[1]/div[1]/span[1]')

    # кнопка "Правила" в разделе "Учебники и Тетради"
    regulations_button = WebElement(
        xpath='//*[@id="minwidth"]/div[5]/div[1]/div[1]/div[1]/div[1]/a[2]/span[2]/span[1]/span[1]')

    # название раздела на странице "Учебники и Тетради"
    regulations_title = WebElement(
        xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/h1[1]')

    # кнопка "Авторы" в горизонтальном меню
    authors_button = WebElement(
        xpath='//*[@id="stab-slider-frame"]/ul[1]/li[2]/a[1]/span[1]')

    # список авторов в результатах поиска
    authors_names = ManyWebElements(
        xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a/span[1]')

    # кнопка выбора автора "Зима Владимир"
    our_author_button = WebElement(
        xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a[2]')

    # кнопка выбора автора "Ленин Владимир Ильич"
    petrov_author_button = WebElement(
        xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a[2]/span[1]')

    # кнопка "Изд-ва" в горизонтальном меню
    publishing_offices_button = WebElement(
        xpath='//*[@id="stab-slider-frame"]/ul[1]/li[3]/a[1]/span[1]')

    # список издательств в результатах поиска
    publishing_offices = ManyWebElements(
        xpath='div[@class="b-search-rubric-items-content"]')

    # кнопка выбора издательста "Правда Севера"
    publishing_office_button = WebElement(
        xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a[2]/span[1]')

    # кнопка "Все книги"
    all_books_button = WebElement(
        xpath='//*[@id="minwidth"]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/a[1]')

    # кнопка "Серии" в горизонтальном меню
    product_series_button = WebElement(
        xpath='//*[@id="stab-slider-frame"]/ul/li[4]/a/span[1]')

    # список серий товаров в результатах поиска
    product_series = ManyWebElements(
        xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a/span[1]')

    # кнопка выбора серии "Тайный город Вадима Панова Эксмо"
    product_part_button = WebElement(
        xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a[39]/span[1]')

    # содержание раздела на открывшейся странице "Тайный город Вадима Панова Эксмо"
    tayniy_gorod = WebElement(
        xpath='//a[@id="thermometer-select"]')


    # кнопка "Видео" в горизонтальном меню
    video_button = WebElement(
        xpath='//*[@id="stab-slider-frame"]/ul[1]/li[9]/a[1]/span[1]')

    # список видео в результатах поиска
    video_products = ManyWebElements(
        xpath='//a[@class="rubric-list-item videobloc-carousel-item js-videoblock-video-show"]')



    # кнопка "Темы" в горизонтальном меню
    themes_button = WebElement(
        xpath='//*[@id="stab-slider-frame"]/ul[1]/li[3]/a[1]/span[1]')

    # список тем в результатах поиска
    themes_products = ManyWebElements(
        xpath='//a[@class="rubric-list-item"]')

    # кнопка "Мамин борщ и бабушкины пироги. Рецепты счастливой кухни от Маши Трауб"
    theme_button = WebElement(
        xpath='//*[@id="rubric-tab"]/div[3]/div[1]/div[3]/a[6]/span[1]')

    # содержание раздела на открывшейся странице "Мамин борщ и бабушкины пироги. Рецепты счастливой кухни от Маши Трауб"
    mom_borsh = WebElement(
        xpath='//*[@id="right-inner"]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]')

