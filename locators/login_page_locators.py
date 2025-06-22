from selenium.webdriver.common.by import By

class LoginPageLocators:

     EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
     PASSWORD_INPUT = (By.CSS_SELECTOR, "input.input__textfield[type='password'][name='Пароль']")
     LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
     FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a.Auth_link__1fOlj[href='/forgot-password']")
     LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")