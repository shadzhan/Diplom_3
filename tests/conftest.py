import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from curl  import Urls
from data import Credentials
from pages.login_page import LoginPage
from locators.login_page_locators import LoginPageLocators
from pages.order_feed_page import OrderFeedPage

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Urls.MAIN_SITE)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(Urls.MAIN_SITE)
    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    """Фикстура для авторизации пользователя."""

    driver.get(Urls.LOGIN_PAGE)

    login_page = LoginPage(driver)
    login_page.wait_for_element(LoginPageLocators.LOGIN_HEADER, timeout=15)
    login_page.login(Credentials.email, Credentials.password)

    driver.get(Urls.MAIN_SITE)
    return driver

@pytest.fixture
def order_feed_page(driver):
    return OrderFeedPage(driver)