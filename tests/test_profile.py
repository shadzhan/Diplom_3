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
    def test_go_to_order_history(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.go_to_profile()
        profile_page.go_to_order_history()

        assert profile_page.is_order_history_section_visible(), "Раздел истории заказов не отображается"

    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.go_to_profile()
        profile_page.logout()

        login_page = LoginPage(driver)
        login_page.should_be_login_url()

        assert login_page.is_current_url_contains("login"), \
            "URL не соответствует странице входа"

    @allure.title("Переход в конструктор из личного кабинета")
    def test_go_to_constructor_from_profile(self, driver, login):
        profile_page = ProfilePage(driver)

        profile_page.go_to_profile()
        profile_page.go_to_constructor()

        current_url = profile_page.get_current_url()
        assert Urls.HOME_PAGE in current_url, \
            f"Не произошел переход на главную страницу. Текущий URL: {current_url}"

    @allure.title("Переход в ленту заказов из личного кабинета")
    def test_go_to_order_feed_from_profile(self, driver, login):
        profile_page = ProfilePage(driver)
        profile_page.go_to_profile()
        profile_page.go_to_order_feed()

        current_url = profile_page.get_current_url()
        assert Urls.ORDER_LIST_PAGE in current_url, \
            f"Не произошел переход на страницу ленты заказов. Текущий URL: {current_url}"

