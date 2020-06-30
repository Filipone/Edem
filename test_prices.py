from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)

a = 1
with_price = []
without_price = []

urls = [
    #"https://edem-shop.by/catalog/srezannye_tsvety/",
    #"https://edem-shop.by/catalog/bukety/",
    #"https://edem-shop.by/catalog/svadebnye_bukety/",
    "https://edem-shop.by/catalog/komnatnye_rasteniya/",
    "https://edem-shop.by/catalog/kompozitsii/"
]

for url in urls:
    print(url.split("/")[4])
    browser.get(url)
    pages = browser.find_elements_by_css_selector("div.pagination a")
    while True:
        prices = browser.find_elements_by_css_selector("span.js_denomination_price")
        orders = browser.find_elements_by_css_selector("span.old_price.instock")
        index = 0
        for price in prices:
            with_price.append(price.text)
            if "0,00" == price.text: print(f"Букет с нулевой ценой: {((browser.find_elements_by_css_selector('a.name'))[index]).text}")
            index += 1
        for order in orders:
            without_price.append(order.text)
        try:
            next_page = browser.find_element_by_css_selector("a.next").click()
            a += 1
            print(f"Страница {a}")
        except Exception:
            print("Больше страниц нету\n")
            break

    print(f"Количество товаров с ценой: {len(with_price)}")
    print(f"Количество товаров под заказ: {len(without_price)}\n")
    a = 1
    with_price = []
    without_price = []

browser.quit()
