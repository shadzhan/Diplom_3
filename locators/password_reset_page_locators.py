from selenium.webdriver.common.by import By

class PasswordResetLocators:
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='Введите новый пароль']")
    SHOW_HIDE_BUTTON = (By.CSS_SELECTOR, "div.input__icon-action")
    RESET_FORM = (By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "div[class*='Modal_modal_overlay']")
    ACTIVE_INPUT_FIELD = (By.CSS_SELECTOR, "div.input_status_active")
