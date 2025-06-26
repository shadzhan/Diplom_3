from selenium.webdriver.common.by import By

class MainPageLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(text(), 'Конструктор')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Лента Заказов']")
    LOGIN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")
    #  - Кнопка "Войти в аккаунт на главной странице"

    INGREDIENT_ITEM = (By.CSS_SELECTOR, "img[alt='Краторная булка N-200i']")
    ORDER_DETAILS_POPUP = (By.CSS_SELECTOR, "img[class*='Modal_modal__ingImage']")
    CLOSE_POPUP_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK")
    INGREDIENT_COUNTER_BUTTON = (By.XPATH, "(//p[contains(@class, 'counter_counter__num__3nue1')])[2]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (By.CSS_SELECTOR, "div[class*='Modal_modal__contentBox']")
    MODAL_OVERLAY = (By.CSS_SELECTOR, "img[alt='loading animation']")
    ORDER_LIST_CONTAINER = (By.CLASS_NAME, "OrderFeed_list__OLh59")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')  # - Кнопка "Личный кабинет"
    CONSTRUCTOR_BASKET = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_NUMBER = (By.CSS_SELECTOR, "h2.Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "button svg[fill='#F2F2F3']")
    INGREDIENT_ITEM_FIRST = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    INGREDIENTS_LIST = (By.XPATH, "//div[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]") # Список ингредиентов


    # Ингредиенты
    SAUCE = (By.XPATH, ".//span[text()='Соусы']")  # локатор раздела "Соусы"
    BUN = (By.XPATH, ".//span[text()='Булки']")  # локатор раздела "Булки"
    FILLING = (By.XPATH, ".//span[text()='Начинки']")  # локатор раздела "Начинки"

