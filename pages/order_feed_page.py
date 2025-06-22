import time

import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.main_page_locators import MainPageLocators
from curl import Urls
from pages.profile_page import ProfilePage
from locators.profile_page_locators import ProfilePageLocators


class OrderFeedPage(BasePage):
    @allure.step("Получить количество заказов за всё время")
    def get_total_orders_count(self):
        return int(self.get_text_on_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNT))

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        return int(self.get_text_on_element(OrderFeedPageLocators.TODAY_ORDERS_COUNT))

    @allure.step("Получить номера заказов в работе")
    def get_in_progress_orders(self):
        return [el.text for el in self.find_elements(OrderFeedPageLocators.IN_PROGRESS_ORDERS)]

    @allure.step("Открыть детали первого заказа")
    def open_first_order_details(self):
        self.click_on_element(OrderFeedPageLocators.ORDER_LIST_FIRST_ORDER)
        time.sleep(2)
        self.wait_for_element(OrderFeedPageLocators.ORDER_DETAILS_MODAL)
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)


    @allure.step("Закрыть детали заказа")
    def close_order_details(self):
        self.click_on_element(OrderFeedPageLocators.MODAL_CLOSE_BUTTON)
        return self


    @allure.step("Проверить, что счетчик заказа увеличился")
    def check_order_counter_increased(self, previous_value):
        current_value = int(self.get_text_on_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNT))
        assert current_value > previous_value, "Счетчик заказов не увеличился"

    @allure.step("Проверить, что счетчик заказа 'Выполнено за сегодня'увеличился")
    def check_order_today_counter_increased(self, previous_value):
        current_value = int(self.get_text_on_element(OrderFeedPageLocators.TODAY_ORDERS_COUNT))
        assert current_value > previous_value, "Счетчик заказов за сегодня не увеличился"


    def is_element_present_order_details(self):
        return self.find_element(OrderFeedPageLocators.ORDER_DETAILS_MODAL)

    @allure.step("Переход на страницу ленты заказов")
    def go_to_order_feed(self):
        time.sleep(3)
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_for_url_contains(Urls.ORDER_LIST_PAGE)
        self.wait_for_element(OrderFeedPageLocators.FEED_CONTAINER)
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)

    @allure.step("Получить номера заказов из истории")
    def get_history_order_numbers(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_for_url_contains(Urls.PROFILE_PAGE)

        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_LINK)
        self.wait_for_element(ProfilePageLocators.ORDER_LIST_CONTAINER)

        order_numbers_elements = self.find_elements(ProfilePageLocators.HISTORY_ORDER_NUMBER)
        order_numbers = [el.text for el in order_numbers_elements]
        return order_numbers

    @allure.step("Получить номера заказов из ленты")
    def get_feed_order_numbers(self):
        self.wait_for_url_contains(Urls.ORDER_LIST_PAGE)
        self.wait_for_element(OrderFeedPageLocators.FEED_CONTAINER)

        order_number_elements = self.find_elements(OrderFeedPageLocators.ORDER_LIST_FIRST_ORDER)
        order_numbers = [el.find_element(*OrderFeedPageLocators.ORDER_NUMBER).text for el in order_number_elements]
        return order_numbers


