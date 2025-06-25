import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from curl import Urls
from locators.main_page_locators import MainPageLocators

class LoginPage(BasePage):

    @allure.step("Открыть страницу логина")
    def open(self):
        self.open_url(f"{Urls.LOGIN_PAGE}")
        self.wait_for_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.send_keys_to_input(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.send_keys_to_input(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажать кнопку 'Войти'")
    def click_login_button(self):
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Нажать ссылку 'Восстановить пароль'")
    def click_forgot_password_link(self):
        self.click_on_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Выполнить полную авторизацию")
    def full_authorization(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Войти в аккаунт")
    def login(self, email, password):
        self.wait_for_element(LoginPageLocators.LOGIN_HEADER, timeout=15)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

        self.wait_for_element(MainPageLocators.ORDER_BUTTON, timeout=15)


    @allure.step("Проверить текущий URL")
    def should_be_login_url(self):
        self.wait_for_url_contains(f"{Urls.LOGIN_PAGE}")

    @allure.step("Проверить переход на страницу восстановления пароля")
    def should_be_forgot_password_page(self):
        self.wait_for_url_contains(f"{Urls.FORGOT_PASSWORD_PAGE}")

    @allure.step("Ожидание загрузки страницы входа")
    def wait_for_login_page_loaded(self):
        self.wait_for_element(LoginPageLocators.LOGIN_HEADER)
        self.wait_for_element(LoginPageLocators.EMAIL_INPUT)
        self.wait_for_element(LoginPageLocators.PASSWORD_INPUT)
