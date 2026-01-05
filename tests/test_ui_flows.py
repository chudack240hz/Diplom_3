"""
Проверка основной функциональности приложения
"""
import allure

from pages.main_page import MainPage


class TestUIFlows:
    """Тесты для проверки основной функциональности"""

    @allure.title('TC-001: Переход по клику на "Конструктор"')
    def test_navigate_to_constructor(self, driver):
        """Проверка перехода на страницу конструктора"""
        main_page = MainPage(driver)
        main_page.click_constructor_button()
        main_page.is_constructor_page()

    @allure.title('TC-002: Переход по клику на "Лента заказов"')
    def test_navigate_to_orders_feed(self, driver):
        """Проверка перехода в раздел ленты заказов"""
        main_page = MainPage(driver)
        main_page.click_orders_feed_button()
        main_page.is_orders_feed_page()

    @allure.title('TC-003: Открытие модального окна с деталями ингредиента')
    def test_open_ingredient_modal(self, driver):
        """Проверка отображения модального окна с деталями ингредиента"""
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.is_ingredient_popup_open()

    @allure.title('TC-004: Закрытие модального окна по крестику')
    def test_close_ingredient_modal(self, driver):
        """Проверка закрытия модального окна с деталями ингредиента"""
        main_page = MainPage(driver)
        main_page.open_ingredient_popup()
        main_page.close_ingredient_popup()
        main_page.is_ingredient_popup_close()

    @allure.title('TC-005: Проверка добавления ингредиента в заказ')
    def test_ingredient_counter_increase(self, driver):
        """Проверка, что цена заказа меняется при добавлении ингредиента"""
        main_page = MainPage(driver)
        main_page.add_ingredient_to_order()
        main_page.check_price()  # Проверяем, что цена изменилась
