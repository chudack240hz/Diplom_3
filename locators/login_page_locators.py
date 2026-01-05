"""Локаторы страницы авторизации"""
from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы элементов на странице входа"""
    RESET_BTN_PAGE = By.XPATH, "//a[normalize-space()='Восстановить пароль']"
    EMAIL_FIELD = By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input"
    PASSWORD_FIELD = By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input"
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']"
