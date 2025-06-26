import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from locators.password_reset_page_locators import PasswordResetLocators
from curl import Urls
import time


class PasswordResetPage(BasePage):
    @allure.step("Проверить, что открыта страница сброса пароля")
    def should_be_password_reset_page(self):
        self.wait_for_url_contains(f"{Urls.MAIN_SITE}{Urls.RESET_PASSWORD_PAGE}")
        self.wait_for_element(PasswordResetLocators.RESET_FORM)
        self.wait_for_element(PasswordResetLocators.PASSWORD_INPUT)

    @allure.step("Проверить подсветку поля пароля")
    def is_password_field_highlighted(self):
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
        self.click_on_element(PasswordResetLocators.PASSWORD_INPUT)

    @allure.step("Проверить наличие текста на странице")
    def is_current_url_contains(self, text):
        return text in self.get_current_url()