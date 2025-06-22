from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    RESET_FORM = (By.XPATH, "//h2[contains(text(), 'Восстановление пароля')]")
    EMAIL_INPUT = (By.CSS_SELECTOR, ".input .input__textfield")
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")

