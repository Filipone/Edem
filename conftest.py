import time
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """Открытие определенного браузера по умолчанию"""
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


LINK_MAIN = "https://edem-shop.by/catalog/bukety/"


@pytest.fixture(scope="session")
def browser(request):
    """Запускаем определенный браузер, добавляем товар в корзину, выбираем дату
        request нужен для выбора браузера"""
    print("\nStart")
    br_name = request.config.getoption("--browser_name")
    if br_name == "chrome":
        print("\nstart chrome browser for test..")
        br = webdriver.Chrome()
    elif br_name == "firefox":
        print("\nstart firefox browser for test..")
        br = webdriver.Firefox()
    else:
        raise pytest.UsageError(f"--browser_name {br_name}, should be chrome or firefox")
    br.implicitly_wait(5)


    # Переход на сайт
    br.get(LINK_MAIN)
    time.sleep(2)

    br.find_element_by_css_selector("div.buts.clearfix>a.add_to").click()
    br.find_element_by_css_selector("a.zakaz").click()
    time.sleep(2)
    br.execute_script("window.scrollBy(0, 400);")

    # Работа в корзине
    time.sleep(1)
    br.find_element_by_css_selector("p.delivery-form__text").click()  # Выбор доставки
    br.find_element_by_css_selector("input#new_order_date").click()  # Выбор дня
    br.execute_script("window.scrollBy(0, 500);")
    time.sleep(1)
    br.find_element_by_css_selector("a.ui-state-default.ui-state-highlight.ui-state-active").click()

    yield br
    print("\nfinish")
    br.quit()

"""
    # Выбор 8 марта
    br.find_element_by_css_selector("span.ui-icon.ui-icon-circle-triangle-e").click()
    time.sleep(1)
    br.find_element_by_link_text('8').click()
"""

