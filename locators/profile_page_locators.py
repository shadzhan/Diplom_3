from selenium.webdriver.common.by import By


class ProfilePageLocators:
    # Основные элементы
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_FEED_BUTTON = (By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and contains(text(),'Лента Заказов')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2' and contains(text(),'Конструктор')]")

    # Индикаторы
    PROFILE_SECTION = (By.CSS_SELECTOR, "div.Profile_profile__3dzvr")
    ORDER_LIST_CONTAINER = (By.CLASS_NAME, "OrderHistory_profileList__374GU")
    HISTORY_ORDER_NUMBER = (By.XPATH, "(//p[@class='text text_type_digits-default'])[33]")