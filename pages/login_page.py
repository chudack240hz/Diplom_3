"""
Методы взаимодействия со страницей авторизации
"""
import allure

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import TIME_WAIT, Urls, user_data
from locators.login_page_locators import LoginPageLocators as LL
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Класс страницы авторизации"""
    
    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_reset_btn(self):
        """Кликает по кнопке восстановления пароля"""
        self.click_to_element(LL.RESET_BTN_PAGE)

    @allure.step('Авторизация пользователя')
    def user_login(self):
        """Выполняет авторизацию с учетными данными по умолчанию"""
        self.login_with_credentials(user_data.email, user_data.password)

    @allure.step('Авторизация пользователя с указанными данными')
    def login_with_credentials(self, email: str, password: str):
        """Выполняет авторизацию с переданными email и паролем"""
        email_input = WebDriverWait(self.driver, TIME_WAIT).until(
            EC.visibility_of_element_located(LL.EMAIL_FIELD)
        )
        email_input.send_keys(email)
        password_input = WebDriverWait(self.driver, TIME_WAIT).until(
            EC.visibility_of_element_located(LL.PASSWORD_FIELD)
        )
        password_input.send_keys(password)
        submit_button = self.driver.find_element(*LL.LOGIN_BUTTON)
        submit_button.click()
        WebDriverWait(self.driver, TIME_WAIT).until(EC.url_to_be(Urls.main_page))

    @allure.step('Проверка перехода на страницу "Восстановить пароль"')
    def assert_forgot_page(self):
        """Проверяет переход на страницу восстановления пароля"""
        assert WebDriverWait(self.driver, 10).until(EC.url_to_be(Urls.login_page))
