from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_1(browser):
    browser.implicitly_wait(10)
    browser.get(link)

    try:
        button = browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    except NoSuchElementException:
        assert False, "There is no add-to-basket button"
    time.sleep(2)
#-m pytest -s -v --language=es test_items.py