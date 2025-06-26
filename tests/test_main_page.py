import allure
import pytest
from pages.main_page import MainPage


@allure.feature("Главная страница")
class TestMainPage:

    @allure.story("Проверка всплывающего окна с деталями ингредиента")
    @allure.title("Открытие и закрытие модального окна ингредиента")
    def test_ingredient_details_popup(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открыть главную страницу"):
            main_page.main_page_loading_wait()

        with allure.step("Кликнуть на ингредиент и дождаться открытия окна"):
            main_page.open_ingredient_details()

        with allure.step("Закрыть модальное окно крестиком"):
            main_page.close_popup()

        assert main_page.is_ingredient_modal_closed(), \
            "Модальное окно с деталями ингредиента не закрылось"


    @allure.title("Проверка добавления ингредиента в конструктор")
    def test_put_ingredient_to_counter(self, driver):
        main_page = MainPage(driver)

        with allure.step("1. Открыть главную страницу и дождаться загрузки"):
            main_page.main_page_loading_wait()

        with allure.step("2. Проверить начальное состояние счетчика"):
            initial_count = main_page.get_ingredient_counter_value()
            assert initial_count == 0, (
                f"Начальный счетчик должен быть 0, фактически: {initial_count}"
            )

        with allure.step("3. Добавить ингредиент в конструктор"):

            main_page.put_ingredient_into_basket()

        with allure.step("4. Проверить обновление счетчика"):
            new_count = main_page.get_ingredient_counter_value()
            assert new_count == initial_count + 2, (
                f"После добавления ингредиента счетчик должен увеличиться на 2, "
                f"фактически: {new_count}"
            )

    @allure.story("Оформление заказа")
    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_place_order(self, driver, login):
        main_page = MainPage(driver)

        with allure.step("Добавить ингредиент в конструктор"):
            main_page.main_page_loading_wait()
            main_page.put_ingredient_into_basket()

        with allure.step("Нажать кнопку оформления заказа"):
            main_page.place_order()

        with allure.step("Проверить появление модального окна заказа"):
            assert main_page.is_order_modal_visible(), \
                "Модальное окно оформления заказа не появилось"

        with allure.step("Проверить, что отображается номер заказа"):
            order_number = main_page.get_order_number()
            assert order_number.isdigit(), "Номер заказа не отображается или некорректен"

        with allure.step("Закрыть модальное окно заказа"):
            main_page.close_order_modal()

        assert main_page.is_order_modal_closed(), \
            "Модальное окно оформления заказа не закрылось"