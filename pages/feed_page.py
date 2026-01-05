"""
Методы взаимодействия со страницей ленты (бургеры)
"""
import allure

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import TIME_WAIT, Urls
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    """Класс страницы ленты (бургеры), содержащий методы для взаимодействия с элементами страницы"""

    @allure.step('Нажать кнопку "Личный кабинет" на странице ленты')
    def click_login_btn(self):
        """Кликает по кнопке 'Личный кабинет' на странице ленты"""
        self.click_to_element(FeedPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Открыть аккаунт из шапки страницы ленты')
    def click_account_btn(self):
        """Открывает аккаунт из шапки страницы ленты"""
        self.click_to_element(FeedPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Открыть первый заказ в ленте')
    def click_order(self):
        """Открывает первый заказ в ленте"""
        self.click_to_element(FeedPageLocators.ORDER_CSS)

    @allure.step('Проверить отображение попапа заказа')
    def is_order_popup_open(self):
        """Проверяет отображение попапа с деталями заказа"""
        assert self.find_element(FeedPageLocators.ORDER_DETAILS_POPUP).is_displayed()

    @allure.step('Проверить открытие страницы конструктора')
    def is_constructor_page(self):
        """Проверяет открытие страницы конструктора"""
        assert WebDriverWait(self.driver, TIME_WAIT).until(EC.url_to_be(Urls.main_page))

    @allure.step('Проверить открытие страницы ленты заказов')
    def is_orders_feed_page(self):
        """Проверяет открытие страницы ленты заказов"""
        assert WebDriverWait(self.driver, TIME_WAIT).until(EC.url_to_be(Urls.feed_page))

    @allure.step('Получить счётчик "Выполнено за всё время"')
    def count_all(self):
        """Возвращает количество заказов за всё время"""
        counter = self.find_element(FeedPageLocators.ALL_TIME_ORDERS_XPATH)
        return int(counter.text)

    @allure.step('Получить счётчик "Выполнено за сегодня"')
    def count_today(self):
        """Возвращает количество заказов за сегодня"""
        counter = self.find_element(FeedPageLocators.TODAY_ORDERS_XPATH)
        return int(counter.text)

    @allure.step('Проверить, что лента заказов пользователя не пуста')
    def check_user_orders(self):
        """Проверяет, что лента заказов пользователя не пуста"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(FeedPageLocators.USER_ORDERS)
        )
        order_elements = self.driver.find_elements(*FeedPageLocators.USER_ORDERS)
        assert len(order_elements) != 0

    @allure.step('Получить текст первого заказа')
    def get_order(self):
        """Возвращает текст первого заказа в ленте"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(FeedPageLocators.ORDER)
        )
        order_element = self.driver.find_element(*FeedPageLocators.ORDER)
        return order_element.text

    @allure.step('Получить номера заказов из колонки "В работе"')
    def get_order_numbers(self):
        """Возвращает список номеров заказов из колонки 'В работе'"""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(FeedPageLocators.ORDER_NUMBERS_CSS_SELECTOR)
        )
        order_elements = self.driver.find_elements(*FeedPageLocators.ORDER_NUMBERS_CSS_SELECTOR)
        numbers = []
        for element in order_elements:
            raw_text = element.text.strip()
            if not raw_text:
                continue
            cleaned = raw_text.lstrip("#").strip()
            normalized = cleaned.lstrip("0") or "0"
            numbers.append(normalized)
        return numbers

    @allure.step('Ожидать появления заказа в колонке "В работе"')
    def wait_order_in_progress(self, order_id: str):
        """Ожидает появления заказа с указанным ID в колонке 'В работе'"""
        WebDriverWait(self.driver, 20).until(
            lambda _: order_id in self.get_order_numbers()
        )
