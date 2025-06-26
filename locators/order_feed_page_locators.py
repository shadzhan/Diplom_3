from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    # Основные разделы
    FEED_CONTAINER = (By.CSS_SELECTOR, "ul.OrderFeed_list__OLh59") # Контейнер с заказами
    ORDER_LIST_FIRST_ORDER = (By.CSS_SELECTOR, "li.OrderHistory_listItem__2x95r:first-of-type")

    # Счётчики
    TOTAL_ORDERS_COUNT = (By.CSS_SELECTOR, "div:nth-child(2) > p.OrderFeed_number__2MbrQ")
    TODAY_ORDERS_COUNT = (By.CSS_SELECTOR, "div:nth-child(3) > p.OrderFeed_number__2MbrQ")

    # Раздел "В работе"
    IN_PROGRESS_ORDER = (By.XPATH, "(//li[contains(@class, 'text_type_digits-default')])[6]")


    # Элементы заказа (для использования внутри заказа)
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")


    # Модальное окно деталей заказа
    ORDER_DETAILS_MODAL = (By.CSS_SELECTOR, "div.Modal_orderBox__1xWdi")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, "section.Modal_modal_opened__3ISw4 button")

