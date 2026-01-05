"""Локаторы главной страницы"""
from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы элементов на главной странице"""
    COOKIES_BTN = By.ID, "rcc-confirm-button"
    LOGIN_BTN_PAGE = By.XPATH, "//button[normalize-space()='Войти в аккаунт']"
    GO_LOGIN = By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]"
    PERSONAL_ACCOUNT = By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"
    MAKE_ORDER = By.XPATH, "//button[text()='Оформить заказ']"
    BREAD_BUTTON = By.XPATH, "//span[contains(text(), 'Булки')]/parent::div"
    SAUCE_BUTTON = By.XPATH, "//span[contains(text(), 'Соусы')]/parent::div"
    FILLING_BUTTON = By.XPATH, "//span[contains(text(), 'Начинки')]/parent::div"
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(text(), 'Конструктор')]"
    ORDERS_FEED_BUTTON = By.XPATH, "//p[contains(text(), 'Лента Заказов')]/ancestor::a"
    INGREDIENT = By.XPATH, "//p[contains(text(), 'Флюоресцентная булка R2-D3')]/ancestor::a"
    INGREDIENT_DETAILS_POPUP = By.CLASS_NAME, "Modal_modal_opened__3ISw4"
    INGREDIENT_DETAILS_CLOSE_BUTTON = By.CLASS_NAME, "Modal_modal__close__TnseK"
    CHECK_POPUP = By.CLASS_NAME, "Modal_modal__close__TnseK"
    PLACE_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']"
    ORDER_SUCCESS_POPUP = By.CLASS_NAME, "Modal_modal_opened__3ISw4"
    BREAD_CSS = By.CSS_SELECTOR, '.BurgerIngredient_ingredient__1TVf6'
    TARGET_CSS = By.CSS_SELECTOR, '.constructor-element__row'
    COUNTER_CSS = By.CSS_SELECTOR, 'p.text.text_type_digits-medium.mr-3'
    MODAL_TITLE_CSS_SELECTOR = By.CSS_SELECTOR, "h2.Modal_modal__title_shadow__3ikwq." \
                                                "Modal_modal__title__2L34m.text.text_type_digits-large.mb-8"
