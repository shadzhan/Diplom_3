class Urls:
    MAIN_SITE = 'https://stellarburgers.nomoreparties.site'
    API_BASE = f'{MAIN_SITE}/api'

    # API эндпоинты
    INGREDIENTS_ENDPOINT = f'{API_BASE}/ingredients'
    PASSWORD_RESET_ENDPOINT = f'{API_BASE}/password-reset'
    FORGOT_PASSWORD_ENDPOINT = f'{API_BASE}/password-reset'
    LOGIN_ENDPOINT = f'{API_BASE}/auth/login'
    LOGOUT_ENDPOINT = f'{API_BASE}/auth/logout'

    # Страницы UI
    HOME_PAGE = 'https://stellarburgers.nomoreparties.site'
    LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login'
    RESET_PASSWORD_PAGE = '/reset-password'
    PROFILE_PAGE = 'https://stellarburgers.nomoreparties.site/account/profile'
    HISTORY_OF_ORDERS_PAGE = 'https://stellarburgers.nomoreparties.site/account/order-history'
    ORDER_LIST_PAGE = 'https://stellarburgers.nomoreparties.site/feed'
    INGREDIENT_PAGE = 'https://stellarburgers.nomoreparties.site/ingredient'
    FORGOT_PASSWORD_PAGE = '/forgot-password'