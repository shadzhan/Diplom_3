import time
import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from curl import Urls


class MainPage(BasePage):

    @allure.step('Дождаться загрузки страницы')
    def main_page_loading_wait(self):
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)

    @allure.step("Переход к разделу 'Конструктор'")
    def go_to_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переход к разделу 'Лента заказов'")
    def go_to_order_feed(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Подождать загрузки списка заказов")
    def wait_for_order_list(self):
        self.wait_for_element(MainPageLocators.ORDER_LIST_CONTAINER)

    @allure.step("Переход в 'Личный кабинет'")
    def go_to_personal_account(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Открыть детали ингредиента по клику")
    def open_ingredient_details(self):
        self.click_on_element(MainPageLocators.INGREDIENT_ITEM)
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element(MainPageLocators.ORDER_DETAILS_POPUP)

    @allure.step("Закрыть всплывающее окно с деталями")
    def close_popup(self):
        self.click_on_element(MainPageLocators.CLOSE_POPUP_BUTTON)
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_into_basket(self):
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element(MainPageLocators.INGREDIENT_ITEM_FIRST)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_ITEM_FIRST, MainPageLocators.CONSTRUCTOR_BASKET)

    @allure.step("Оформить заказ (если пользователь залогинен)")
    def place_order(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)
        self.wait_for_element(MainPageLocators.ORDER_MODAL)

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_button(self):
        self.click_on_element(MainPageLocators.LOGIN_ACCOUNT_BUTTON)

    @allure.step("Проверка загрузки страницы 'Личный кабинет'")
    def wait_for_profile_page_load(self):
        self.wait_for_url_contains(f"{Urls.MAIN_SITE}{Urls.PROFILE_PAGE}")

    @allure.step("Ожидание авторизованного состояния")
    def wait_for_authorized_state(self):
        self.wait_for_element(MainPageLocators.ORDER_BUTTON)



    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter_value(self):
        counter_element = self.wait_for_element(MainPageLocators.INGREDIENT_COUNTER_BUTTON)
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
        return int(counter_element.text) if counter_element.text else 0

    @allure.step('Put ingredient into basket')
    def put_ingredient_into_basket(self):
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element(MainPageLocators.INGREDIENT_ITEM)
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_ITEM, MainPageLocators.CONSTRUCTOR_BASKET)

        self.wait_for_element(MainPageLocators.INGREDIENT_COUNTER_BUTTON)

    @allure.step("Проверить видимость модального окна заказа")
    def is_order_modal_visible(self):
        return self.find_element(MainPageLocators.ORDER_MODAL)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        self.wait_for_element(MainPageLocators.MODAL_OVERLAY)
        self.wait_for_element_hide(MainPageLocators.MODAL_OVERLAY)
        order_number_element = self.wait_for_element(MainPageLocators.ORDER_NUMBER)
        return order_number_element.text

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.click_on_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Проверка закрытия модального окна заказа")
    def is_order_modal_closed(self):
        return self.wait_for_element_hide(MainPageLocators.ORDER_MODAL)

    @allure.step("Проверить закрытия модального окна с деталями ингредиента")
    def is_ingredient_modal_closed(self):
        return self.wait_for_element_hide(MainPageLocators.ORDER_DETAILS_POPUP)

