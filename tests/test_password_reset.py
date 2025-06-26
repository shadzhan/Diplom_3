import allure
import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.password_reset_page import PasswordResetPage
from helper import generate_random_email



@allure.feature("Восстановление пароля")
@allure.story("Проверка функционала восстановления пароля")
class TestPasswordRecovery:
    @allure.title("Проверка перехода на страницу восстановления пароля")
    def test_navigate_to_password_recovery(self, driver):
        with allure.step("1. Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()

        with allure.step("2. Кликнуть 'Личный кабинет'"):
            main_page.go_to_personal_account()

        with allure.step("3. Перейти на страницу восстановления пароля"):
            login_page = LoginPage(driver)
            login_page.click_forgot_password_link()

        with allure.step("4. Проверить загрузку страницы восстановления пароля"):
            recovery_page = ForgotPasswordPage(driver)
            recovery_page.should_be_forgot_password_page()

            assert recovery_page.is_current_url_contains("forgot-password"), \
                f"Ожидался переход на страницу восстановления пароля. Текущий URL: {recovery_page.get_current_url()}"

    @allure.title("Восстановление пароля по email")
    def test_password_reset_with_email(self, driver):
        random_email = generate_random_email()
        with allure.step("1. Перейти на страницу восстановления пароля"):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
            main_page.click_login_button()

            login_page = LoginPage(driver)
            login_page.click_forgot_password_link()

        with allure.step(f"2. Ввести сгенерированный email ({random_email}) и отправить форму"):
            forgot_password_page = ForgotPasswordPage(driver)
            forgot_password_page.should_be_forgot_password_page()
            forgot_password_page.enter_email(random_email)
            forgot_password_page.click_recover_button()

        with allure.step("3. Проверить переход на страницу сброса пароля"):
            password_reset_page = PasswordResetPage(driver)
            password_reset_page.should_be_password_reset_page()

            assert password_reset_page.is_current_url_contains("reset-password"), \
                f"Ожидался переход на страницу сброса пароля. Текущий URL: {password_reset_page.get_current_url()}"

    @allure.title("Проверка функционала показа/скрытия пароля")
    def test_password_visibility_toggle(self, driver):
        random_email = generate_random_email()

        with allure.step("1. Перейти на страницу восстановления пароля"):
            main_page = MainPage(driver)
            main_page.main_page_loading_wait()
            main_page.click_login_button()

            login_page = LoginPage(driver)
            login_page.click_forgot_password_link()

        with allure.step(f"2. Ввести сгенерированный email ({random_email}) и отправить форму"):
            forgot_password_page = ForgotPasswordPage(driver)
            forgot_password_page.should_be_forgot_password_page()
            forgot_password_page.enter_email(random_email)
            forgot_password_page.click_recover_button()

        with allure.step("3. Проверить загрузку страницы сброса пароля"):
            reset_password_page = PasswordResetPage(driver)
            reset_password_page.should_be_password_reset_page()

        with allure.step("4. Проверить подсветку поля при клике на иконку"):
            assert reset_password_page.is_password_field_highlighted(), \
                "Поле пароля не подсвечивается при активации"
