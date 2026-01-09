"""Базовый класс страницы с общими взаимодействиями с веб-элементами"""
from typing import Tuple, Any

from selenium.common import ElementClickInterceptedException, UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс страницы с общими взаимодействиями с веб-элементами"""
    def __init__(self, driver: Any) -> None:
        """Инициализация базового класса страницы"""
        self.driver = driver

    def find_element(self, locator: Tuple[str, str]) -> WebElement:
        """Поиск видимого элемента на странице"""
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    def close_cookies_banner(self) -> None:
        """Закрывает баннер cookies, если он присутствует"""
        cookies = self.driver.find_elements(By.ID, "rcc-confirm-button")
        if cookies:
            cookies[0].click()

    def click_to_element(self, locator: Tuple[str, str], timeout: int = 10) -> None:
        """Клик на элемент с обработкой исключений"""
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        try:
            self.driver.find_element(*locator).click()
        except ElementClickInterceptedException:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            try:
                element.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", element)
        except UnexpectedAlertPresentException:
            alert = self.driver.switch_to.alert
            alert.dismiss()
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            self.driver.find_element(*locator).click()

    def get_text(self, locator: Tuple[str, str]) -> str:
        """Получение текста из видимого элемента"""
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator)).text

    def set_text(self, locator: Tuple[str, str], text: str) -> None:
        """Ввод текста в кликабельный элемент"""
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).send_keys(text)

    def scroll(self, locator: Tuple[str, str]) -> None:
        """Прокрутка страницы до указанного элемента"""
        element = self.find_element(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_url(self) -> str:
        """Получение текущего URL страницы"""
        return self.driver.current_url

    def wait_navigating_url(self, url: str) -> None:
        """Ожидание загрузки страницы по указанному URL"""
        WebDriverWait(self.driver, 5).until(EC.url_to_be(url))

    def switch_to_window(self) -> None:
        """Переключение на новое окно браузера"""
        return self.driver.switch_to.window(self.driver.window_handles[1])
