"""Локаторы главной страницы"""
from selenium.webdriver.common.by import By


class FeedPageLocators:
    """Локаторы элементов на странице заказов"""
    COOKIES_BTN = By.ID, "rcc-confirm-button"
    LOGIN_BTN_PAGE = By.XPATH, "//button[normalize-space()='Войти в аккаунт']"
    GO_LOGIN = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"
    PERSONAL_ACCOUNT = By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"
    MAKE_ORDER = By.XPATH, "//button[text()='Оформить заказ']"
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(), 'Конструктор')]"
    ORDER_CSS = By.CLASS_NAME, 'OrderHistory_listItem__2x95r'
    ORDER_DETAILS_POPUP = By.CLASS_NAME, 'Modal_modal_opened__3ISw4'
    USER_ORDERS = By.CLASS_NAME, 'OrderFeed_orderList__cBvyi'
    ORDER = By.CLASS_NAME, 'text_type_digits-default'
    ORDERS_FEED_BUTTON = By.XPATH, "//p[contains(text(), 'Лента Заказов')]/ancestor::a"
    ALL_TIME_ORDERS_XPATH = By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/" \
                                      "following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    TODAY_ORDERS_XPATH = By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/" \
                                   "following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    ORDER_NUMBERS_CSS_SELECTOR = By.CSS_SELECTOR, \
        "ul.OrderFeed_list__OLh59 div.OrderHistory_textBox__3lgbs > p.text.text_type_digits-default"
