"""Тесты функциональности ленты заказов"""
import allure

from helpers.api_helpers import delete_user, get_latest_order_number
from helpers.ui_helpers import authorize_new_user, place_order
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestFeedFunctionality:
    """Тесты для проверки функциональности ленты заказов"""
    
    @allure.title('TC-001: Счетчик "Выполнено за сегодня" увеличивается после нового заказа')
    def test_count_today_increases_on_new_order(self, driver):
        """Проверка увеличения счетчика выполненных заказов за текущий день"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        user = authorize_new_user(main_page, login_page)
        try:
            main_page.click_orders_feed_button()
            count_today = feed_page.count_today()

            main_page.click_constructor_button()
            place_order(main_page)

            main_page.click_orders_feed_button()
            count_today_new = feed_page.count_today()
            assert count_today_new > count_today, (
                'Счетчик "Выполнено за сегодня" не увеличился после создания нового заказа'
            )
        finally:
            delete_user(user)

    @allure.title('TC-002: Счетчик "Выполнено за все время" увеличивается после нового заказа')
    def test_count_all_increases_on_new_order(self, driver):
        """Проверка увеличения общего счетчика выполненных заказов"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        user = authorize_new_user(main_page, login_page)
        try:
            main_page.click_orders_feed_button()
            count_all = feed_page.count_all()

            main_page.click_constructor_button()
            place_order(main_page)

            main_page.click_orders_feed_button()
            count_all_new = feed_page.count_all()
            assert count_all_new > count_all, (
                'Общий счетчик выполненных заказов не увеличился после создания нового заказа'
            )
        finally:
            delete_user(user)

    @allure.title('TC-003: Новый заказ отображается в колонке "В работе"')
    def test_order_appears_in_progress_section(self, driver):
        """Проверка отображения нового заказа в разделе 'В работе'"""
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        feed_page = FeedPage(driver)

        user = authorize_new_user(main_page, login_page)
        try:
            main_page.click_constructor_button()
            place_order(main_page)
            latest_order_number = get_latest_order_number(user)

            main_page.click_orders_feed_button()
            feed_page.wait_order_in_progress(latest_order_number)
            orders = feed_page.get_order_numbers()
            assert latest_order_number in orders, (
                f"Заказ с ID {latest_order_number} не отображается в разделе 'В работе'"
            )
        finally:
            delete_user(user)
