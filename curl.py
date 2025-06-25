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
    HOME_PAGE = f'{MAIN_SITE}/'
    LOGIN_PAGE = f'{MAIN_SITE}/login'
    RESET_PASSWORD_PAGE = '/reset-password'
    PROFILE_PAGE = f'{MAIN_SITE}/account/profile'
    HISTORY_OF_ORDERS_PAGE = f'{MAIN_SITE}/account/order-history'
    ORDER_LIST_PAGE = f'{MAIN_SITE}/feed'
    INGREDIENT_PAGE = f'{MAIN_SITE}/ingredient'
    FORGOT_PASSWORD_PAGE = '/forgot-password'