"""
Локаторы главной страницы
"""
import os
import pytest

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.common.exceptions import WebDriverException

from helpers.api_helpers import create_api_user, delete_user


@pytest.fixture(scope='function')
def driver():
    """Фикстура для инициализации и завершения браузера"""
    browser = os.getenv('BROWSER', 'firefox').lower()

    if browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")

        try:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        except WebDriverException:
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        try:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        except WebDriverException:
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser}")

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def api_user():
    """Создание и удаление тестового пользователя"""
    user = create_api_user()
    yield user
    delete_user(user)
