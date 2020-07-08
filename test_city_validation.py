import time
import pytest


CITIES_20_BYN = [
    "Белая Лужа", "Глинище", pytest.param("Хрень", marks=pytest.mark.xfail),
    "Прудок", "Красный Октябрь", "Новосёлки", "Новосёлки", "Старая Мётча",
    "Белое Болото", "Старина", "Брили", "Костюки", "Жерствянка",
    "Лавники", "Каменка", "Большая Тростяница", "Малая Тростяница",
    "Заболотье", "Стрелковцы", "Тимки", "Садовщина", "Пасека",
    "Блонь", "Юзефово", "Лесная поляна", "Раковцы", "Судоль", "Будагово",
    "Михайлово", "Михайлово, неманицкий сельсовет", "Лобачиха",
    "Домостроитель", "Ново-лесуны", "Швейник-2011", "Фруктовый",
    "Кургановка", "Ланковщина", "Зорька", "Ветеран-Шилино", "Шилино",
    "Гребло", "Ярцевка", "Зелёная Дубрава", "Аскерки", "Добрицкое",
    "Завалы", "Сивица", "Рубленики", "Новый Посёлок", "Барановка",
    "Перстень", "Козловка", "Красное", "Забашевка", "Застенок",
    "Слободка", "Смолье", "Заручье", "Дружный Ландыш", "Криница-88",
    "Строитель-Тарасики", "Дзержинец", "Лесная Поляна-88", "Аккорд-88",
    "Восход", "Экран-Тарасики", "Тарасики", "Солнечный-2", "Меркурий-2002",
    "Патриот-Берёзка", "Тарасик", "Прогресс-2001", "Бродовка", "Веселово",
    "Забашевичи", "Зембин", "Кищина Слобода", "Кострица", "Кричино", "Лошница",
    "Ляховка", "Новая Мётча", "Новосады"
]

@pytest.mark.parametrize("city", CITIES_20_BYN)
def test_cities20byn_validation(browser, city):
    """Проверка валидации и стоимости городов из списка за 20руб"""
    input_city = browser.find_element_by_css_selector("input#locality")
    input_city.clear()
    input_city.send_keys(city)

    response = browser.find_element_by_css_selector("input#locality + span.fields__text")
    response.click()
    time.sleep(1)
    delivery_prise = browser.find_element_by_css_selector("span.js_delivery").text

    print(city)
    assert "Город, посёлок" in browser.find_element_by_css_selector(
        "input#locality + span.fields__text").text, f"Валидацию не прошел город: {city}"

    print(delivery_prise)
    assert "20,00" in delivery_prise, "Стоимсоть доставки не верна"


CITIES_10_BYN = [
    "Большое Стахово", "Большая Ухолода", "Бытча", "Гливин", "Дубовый лог",
    "Житьково", "Жодино", "Изобка", "Малое Стахово", "Малая Ухолода", "Неманица",
    "Пересады", "Погодица", "Подберезье", "Светлая Роща", "Стайки", "Студёнка",
    "Упиревичи", "Лещины", "Дубени", "Селище", "Любатовщина", "Прудище", "Брусы",
    "Горелица", "Залесье", "Струпень", "Ельница", "Верески", "Круглое", "Селитренка",
    "Липки", "Стаи", "Проходы"
]


@pytest.mark.parametrize("city", CITIES_10_BYN)
def test_cities10byn_validation(browser, city):
    """Проверка валидации и стоимости городов из списка за 10руб"""
    input_city = browser.find_element_by_css_selector("input#locality")
    input_city.clear()
    input_city.send_keys(city)

    response = browser.find_element_by_css_selector("input#locality + span.fields__text")
    response.click()
    time.sleep(1)
    delivery_prise = browser.find_element_by_css_selector("span.js_delivery").text

    print(city)
    assert "Город, посёлок" in browser.find_element_by_css_selector(
        "input#locality + span.fields__text").text, f"Валидацию не прошел город: {city}"

    print(delivery_prise)
    assert "10,00" in delivery_prise, "Стоимсоть доставки не верна"


CITIES_5_BYN = [
    'Борисов', 'Пчельник', 'Остров', 'Дудинка', 'Печи', 'Тарасовка',
    'Углы', 'Гора', 'Старо Борисов', 'Демидовка'
]


@pytest.mark.parametrize("city", CITIES_5_BYN)
@pytest.mark.smoke
def test_cities5byn_validation(browser, city):
    """Проверка валидации и стоимости городов из списка за 5руб"""
    input_city = browser.find_element_by_css_selector("input#locality")
    input_city.clear()
    input_city.send_keys(city)

    response = browser.find_element_by_css_selector("input#locality + span.fields__text")
    response.click()
    time.sleep(1)
    delivery_prise = browser.find_element_by_css_selector("span.js_delivery").text

    try:
        print(city)
        print(delivery_prise)
        assert "Город, посёлок" in browser.find_element_by_css_selector(
            "input#locality + span.fields__text").text, f"Валидацию не прошел город: {city}"
    finally:
        assert "бесплатно" in delivery_prise, f"Стоимость доставки у города {city} не верна"
