import pytest
import time


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--log-level=DEBUG')

    return chrome_options


@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    browser.set_window_size(1360, 860)

    # Return browser instance to test case:
    yield browser

# @pytest.fixture(autouse=True)
# def time_delta():
#     start_time = datetime.now()
#     yield
#     end_time = datetime.now()
#     print (f"\nТест шел: {end_time - start_time}")