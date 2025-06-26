import allure
from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordLocators
from curl import Urls


class ForgotPasswordPage(BasePage):
    @allure.step("Проверить, что открыта страница восстановления пароля")
    def should_be_forgot_password_page(self):
        self.wait_for_url_contains(Urls.FORGOT_PASSWORD_PAGE)
        self.wait_for_element(ForgotPasswordLocators.RESET_FORM)

    @allure.step("Ввести email для восстановления пароля")
    def enter_email(self, email):
        self.wait_for_element(ForgotPasswordLocators.EMAIL_INPUT)
        self.send_keys_to_input(ForgotPasswordLocators.EMAIL_INPUT, email)

    @allure.step("Кликнуть по кнопке «Восстановить»")
    def click_recover_button(self):
        self.click_on_element(ForgotPasswordLocators.RECOVER_BUTTON)

    @allure.step("Проверить наличие текста на странице")
    def is_current_url_contains(self, text):
        return text in self.get_current_url()