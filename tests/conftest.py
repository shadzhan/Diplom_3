import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from curl  import Urls
from data import Credentials
from pages.login_page import LoginPage



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


    return driver

@pytest.fixture()
def login(driver):
    """
    Фикстура для авторизации пользователя.
    """
    login_page = LoginPage(driver)
    login_page.login(Credentials.email,Credentials.password)

    return driver
