from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_guest_should_see_add_to_basket_button(browser):
    try:
        browser.get(link)
        button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form>button")

    except NoSuchElementException:
        assert False, "Кнопка 'Добавить в корзину' не найдена"





