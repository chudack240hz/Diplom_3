"""
Методы взаимодействия с главной страницей
"""
import allure
from pathlib import Path

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import TIME_WAIT, Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """Класс страницы конструктора бургеров, содержащий методы для взаимодействия с элементами страницы"""
    
    @allure.step('Авторизация')
    def click_login_btn(self):
        """Клик по кнопке входа в аккаунт на главной странице"""
        self.click_to_element(MainPageLocators.GO_LOGIN)

    @allure.step('Клик на кнопку "Личный кабинет" в шапке главной')
    def click_account_btn(self):
        """Клик по кнопке перехода в личный кабинет в шапке сайта"""
        self.click_to_element(MainPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Клик на "Конструктор"')
    def click_constructor_button(self):
        """Клик по кнопке перехода в раздел конструктора бургеров"""
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Клик на "Лента заказов"')
    def click_orders_feed_button(self):
        """Клик по кнопке перехода в раздел ленты заказов"""   
        self.close_cookies_banner()
        self.click_to_element(MainPageLocators.ORDERS_FEED_BUTTON)
        WebDriverWait(self.driver, 20).until(EC.url_contains("/feed"))

    @allure.step('Клик по ингредиенту')
    def click_ingredient(self):
        """Клик по ингредиенту в конструкторе бургеров. Открывает модальное окно с детальной информацией об ингредиенте"""
        self.click_to_element(MainPageLocators.INGREDIENT)

    @allure.step('Проверка открытия попапа с деталями ингредиента')
    def is_ingredient_popup_open(self):
        """Проверяет, открыто ли модальное окно с деталями ингредиента"""
        assert self.find_element(MainPageLocators.INGREDIENT_DETAILS_POPUP).is_displayed()

    @allure.step('Проверка закрытия попапа с деталями ингредиента')
    def is_ingredient_popup_close(self):
        """Проверяет, закрыто ли модальное окно с деталями ингредиента"""
        elements = self.driver.find_elements(*MainPageLocators.INGREDIENT_DETAILS_POPUP)
        assert len(elements) == 0

    @allure.step('Открытие попапа с ингредиентом')
    def open_ingredient_popup(self):
        """Открывает модальное окно с деталями ингредиента"""
        self.click_ingredient()

    @allure.step('Закрытие попапа с ингредиентом')
    def close_ingredient_popup(self):
        """Закрывает модальное окно с деталями ингредиента"""
        self.click_to_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    @allure.step('Закрытие попапа с заказом')
    def close_check_popup(self):
        """Закрывает модальное окно с информацией о заказе"""
        self.click_to_element(MainPageLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)
        WebDriverWait(self.driver, TIME_WAIT).until(
            EC.invisibility_of_element_located(MainPageLocators.ORDER_SUCCESS_POPUP)
        )

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient_to_order(self):
        """Добавляет ингредиент в заказ с помощью перетаскивания"""
        source_element = self.find_element(MainPageLocators.BREAD_CSS)
        target_element = self.find_element(MainPageLocators.TARGET_CSS)

        # ActionChains некорректно работает с перетаскиванием элементов
        script_path = Path(__file__).resolve().parent.parent / "scripts" / "drag_and_drop.js"
        with script_path.open("r", encoding="utf-8") as f:
            javascript = f.read()
        self.driver.execute_script(javascript, source_element, target_element)

    @allure.step('Оформление заказа')
    def place_order(self):
        """Оформляет заказ, нажимая на кнопку 'Оформить заказ'"""
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Проверка успешного оформления заказа')
    def is_order_placed(self):
        """Проверяет, успешно ли оформлен заказ"""
        assert self.find_element(MainPageLocators.ORDER_SUCCESS_POPUP).is_displayed()

    @allure.step('Проверка, что открыта страница "Конструктор"')
    def is_constructor_page(self):
        """Проверяет, что текущая страница - это страница конструктора бургеров"""
        assert WebDriverWait(self.driver, TIME_WAIT).until(EC.url_to_be(Urls.main_page))

    @allure.step('Проверка, что открыта страница "Лента заказов"')
    def is_orders_feed_page(self):
        """Проверяет, что текущая страница - это страница ленты заказов"""
        assert WebDriverWait(self.driver, TIME_WAIT).until(EC.url_to_be(Urls.feed_page))

    @allure.step('Получение id заказа')
    def get_feed_id(self):
        """Получает идентификатор заказа из модального окна"""
        def order_number_ready(driver):
            text = driver.find_element(*MainPageLocators.MODAL_TITLE_CSS_SELECTOR).text.strip()
            if text and text != "9999":
                return text
            return False

        return WebDriverWait(self.driver, 60).until(order_number_ready)
    @allure.step('Проверка, что изменилась цена')
    def check_price(self):
        """Проверяет, что цена заказа изменилась (не равна нулю)"""
        count_element = self.find_element(MainPageLocators.COUNTER_CSS)
        count_text = count_element.text
        assert count_text != "0"
