import allure
import pytest
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from curl import Urls
from data import Credentials
from pages.main_page import MainPage


@allure.feature("Личный кабинет")
class TestPersonalAccount:

    @allure.title("Переход в личный кабинет авторизованного пользователя")
    def test_go_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.main_page_loading_wait()

        profile_page = ProfilePage(driver)
        profile_page.go_to_profile()

        assert profile_page.should_be_profile_page(), "Страница профиля не загружена"

    @allure.title("Переход в историю заказов")
    @allure.description("Проверка перехода в раздел истории заказов")
    def test_go_to_order_history(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.go_to_profile()
        profile_page.go_to_order_history()

        assert profile_page.is_order_history_section_visible(), "Раздел истории заказов не отображается"

    @allure.title("Выход из аккаунта")
    @allure.description("Проверка выхода из аккаунта по кнопке 'Выход'")
    def test_logout(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.go_to_profile()
        profile_page.logout()

        login_page = LoginPage(driver)
        login_page.should_be_login_url()

    @allure.title("Переход в конструктор из личного кабинета")
    @allure.description("Проверка перехода в конструктор через клик по кнопке")
    def test_go_to_constructor_from_profile(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.go_to_profile()
        profile_page.go_to_constructor()

        assert Urls.HOME_PAGE in driver.current_url, "Не произошел переход на главную страницу"

    @allure.title("Переход в ленту заказов из личного кабинета")
    @allure.description("Проверка перехода в ленту заказов через клик по кнопке")
    def test_go_to_order_feed_from_profile(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.go_to_profile()
        profile_page.go_to_order_feed()

        current_url = driver.current_url
        assert Urls.ORDER_LIST_PAGE in current_url, \
            f"Не произошел переход на страницу ленты заказов. Текущий URL: {current_url}"
