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
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNT)
        return int(self.get_text_on_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNT))

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        return int(self.get_text_on_element(OrderFeedPageLocators.TODAY_ORDERS_COUNT))

    @allure.step("Получить последний номер заказа в разделе 'В работе'")
    def get_in_progress_order(self):
        self.wait_for_element(OrderFeedPageLocators.IN_PROGRESS_ORDER)
        elements = self.find_elements(OrderFeedPageLocators.IN_PROGRESS_ORDER)
        return elements[-1].text

    @allure.step("Открыть детали первого заказа")
    def open_first_order_details(self):
        self.click_on_element(OrderFeedPageLocators.ORDER_LIST_FIRST_ORDER)
        self.wait_for_element(OrderFeedPageLocators.ORDER_DETAILS_MODAL)
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)


    @allure.step("Закрыть детали заказа")
    def close_order_details(self):
        self.click_on_element(OrderFeedPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Подождать, пока счетчик увеличится")
    def wait_for_counter_update(self, previous_value, locator, timeout=10):
        def condition():
            current_value = int(self.get_text_on_element(locator))
            return current_value > previous_value

        self.wait_for_condition(condition, timeout=timeout)
        return self.get_text_on_element(locator)

    @allure.step("Проверить, что счетчик заказа увеличился")
    def check_order_counter_increased(self, previous_value):
        self.wait_for_counter_update(previous_value, OrderFeedPageLocators.TOTAL_ORDERS_COUNT)
        current_value = int(self.get_text_on_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNT))
        return current_value > previous_value, "Счетчик заказов не увеличился"

    @allure.step("Проверить, что счетчик заказа 'Выполнено за сегодня'увеличился")
    def check_order_today_counter_increased(self, previous_value):
        self.wait_for_counter_update(previous_value, OrderFeedPageLocators.TODAY_ORDERS_COUNT)
        current_value = int(self.get_text_on_element(OrderFeedPageLocators.TODAY_ORDERS_COUNT))
        return current_value > previous_value, "Счетчик заказов за сегодня не увеличился"


    def is_element_present_order_details(self):
        return self.find_element(OrderFeedPageLocators.ORDER_DETAILS_MODAL)

    @allure.step("Переход на страницу ленты заказов")
    def go_to_order_feed(self):
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
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

    @allure.step("Проверка присутствия всех указанных номеров в ленте")
    def are_orders_displayed_in_feed(self, order_numbers):
        feed_order_numbers = self.get_feed_order_numbers()
        return all(order_num in feed_order_numbers for order_num in order_numbers)

    def is_order_modal_closed(self):
        return self.wait_for_element_hide(OrderFeedPageLocators.ORDER_DETAILS_MODAL)
