import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from curl import Urls
from locators.main_page_locators import MainPageLocators
import time


class ProfilePage(BasePage):

    @allure.step("Переход в раздел 'История заказов'")
    def go_to_order_history(self):
        self.wait_for_element(ProfilePageLocators.ORDER_HISTORY_LINK)
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_LINK)
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)

    @allure.step("Проверка загрузки страницы 'История заказов'")
    def wait_for_history_oder_page_load(self):
        self.wait_for_element(ProfilePageLocators.ORDER_LIST_CONTAINER)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.wait_for_element(ProfilePageLocators.LOGOUT_BUTTON)
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
        self.click_on_element(ProfilePageLocators.LOGOUT_BUTTON)

    @allure.step("Проверить переход в конструктор")
    def go_to_constructor(self):
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
        self.click_on_element(ProfilePageLocators.CONSTRUCTOR_BUTTON)
        self.wait_for_url_contains(Urls.HOME_PAGE)

    @allure.step("Проверить переход в ленту заказов")
    def go_to_order_feed(self):
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
        self.click_on_element(ProfilePageLocators.ORDER_FEED_BUTTON)
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_url_contains(Urls.ORDER_LIST_PAGE)

    @allure.step("Проверить, что это страница профиля")
    def should_be_profile_page(self):
        self.wait_for_url_contains(Urls.PROFILE_PAGE)
        self.wait_for_element(ProfilePageLocators.ORDER_HISTORY_LINK)
        return True

    @allure.step("Переход в личный кабинет")
    def go_to_profile(self):
        self.wait_for_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_url_contains(Urls.PROFILE_PAGE)
        self.wait_for_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step("Проверка отображения раздела 'История заказов'")
    def is_order_history_section_visible(self):
        return self.wait_for_element(ProfilePageLocators.ORDER_LIST_CONTAINER)


    @allure.step("Проверить наличие текста на странице")
    def is_current_url_contains(self, text):
        return text in self.get_current_url()
