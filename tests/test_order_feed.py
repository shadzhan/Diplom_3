import allure
import pytest
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from data import TestData


@allure.feature("Лента заказов")
class TestMainPage:

    @allure.title("Проверка открытия и закрытия деталей заказа")
    def test_open_order_details(self, driver, login, order_feed_page):
        with allure.step("1. Перейти на страницу ленты заказов"):
            order_feed_page.go_to_order_feed()

        with allure.step("2. Открыть детали первого заказа"):
            order_feed_page.open_first_order_details()

        with allure.step("3. Закрыть модальное окно"):
            order_feed_page.close_order_details()

            assert order_feed_page.is_order_modal_closed(), "Модальное окно с деталями заказа не закрылось"

    @allure.title('Проверка отображения заказов из истории в ленте заказов')
    def test_orders_from_history_displayed_in_feed(self, driver, login, order_feed_page):
        with allure.step("Получить номера заказов из истории заказов"):
            history_orders = order_feed_page.get_history_order_numbers()

        with allure.step("Убедиться, что в истории есть заказы"):
            assert history_orders, "В истории заказов нет ни одного заказа"

        with allure.step("Перейти на страницу ленты заказов"):
            order_feed_page.go_to_order_feed()

        with allure.step("Проверить, что все заказы из истории отображаются в ленте"):
            assert order_feed_page.are_orders_displayed_in_feed(history_orders), (
                "Не все заказы из истории отображаются в ленте"
            )

    @allure.title('Проверка увеличения счетчика "Выполнено за всё время"')
    def test_total_orders_counter_increases(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Получить начальное значение счетчика"):
            order_feed_page.go_to_order_feed()
            initial_total = order_feed_page.get_total_orders_count()

        with allure.step("Создать новый заказ"):
            main_page.add_ingredient_into_basket()
            main_page.place_order()
            main_page.close_popup()

        with allure.step("Дождаться обновления счетчика"):
            order_feed_page.check_order_counter_increased(initial_total)
            updated_total = order_feed_page.get_total_orders_count()

        with allure.step("Проверить увеличение счетчика"):
            assert updated_total > initial_total, f"Счетчик не увеличился: {initial_total} → {updated_total}"


    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_today_orders_counter_increases(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Получить начальное значение счетчика"):
            order_feed_page.go_to_order_feed()
            initial_today = order_feed_page.get_today_orders_count()

        with allure.step("Создать новый заказ"):
            main_page.add_ingredient_into_basket()
            main_page.place_order()
            main_page.close_popup()

        with allure.step("Дождаться обновления счетчика"):
            order_feed_page.check_order_today_counter_increased(initial_today)
            updated_today = order_feed_page.get_today_orders_count()

        with allure.step("Проверить увеличение счетчика"):
            assert updated_today> initial_today, f"Счетчик не изменился: {initial_today} → {updated_today}"


    @allure.title("Заказ появляется в разделе 'В работе' после оформления")
    def test_order_appears_in_progress_section(self, driver, login, order_feed_page):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        with allure.step("Создать новый заказ"):
            main_page.add_ingredient_into_basket()
            main_page.place_order()

        with allure.step("Получить номер созданного заказа"):
            order_number = main_page.get_order_number()
            main_page.close_order_modal()

        with allure.step("Перейти в ленту заказов"):
            order_feed_page.go_to_order_feed()

        with allure.step("Проверить появление заказа в разделе 'В работе'"):
            order_feed_page.get_in_progress_order()

            in_progress_order = order_feed_page.get_in_progress_order()

            assert order_number in in_progress_order, (
                f"Заказ {order_number} не найден в разделе 'В работе'. "
                f"Текущие заказы: {in_progress_order}"
            )

