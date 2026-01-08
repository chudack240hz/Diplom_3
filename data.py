import random
import string
from datetime import datetime, timedelta

TIME_WAIT = 10

class Urls:
    main_page = 'https://stellarburgers.education-services.ru/'
    feed_page = 'https://stellarburgers.education-services.ru/feed'
    login_page = 'https://stellarburgers.education-services.ru/login'
    user_page = 'https://stellarburgers.education-services.ru/account/profile'
    recover_page = 'https://stellarburgers.education-services.ru/forgot-password'
    reset_page = 'https://stellarburgers.education-services.ru/reset-password'


class DataGenerator:
    """Класс для генерации тестовых данных"""
    
    @staticmethod
    def random_string(length=8, letters=True, digits=True):
        """Генерация случайной строки"""
        chars = ''
        if letters:
            chars += string.ascii_letters
        if digits:
            chars += string.digits
        return ''.join(random.choice(chars) for _ in range(length))
    
    @staticmethod
    def random_email(domain='example.com'):
        """Генерация случайного email"""
        username = DataGenerator.random_string(8, True, True).lower()
        return f"{username}@{domain}"
    
    @staticmethod
    def random_password(length=10):
        """Генерация случайного пароля"""
        chars = string.ascii_letters + string.digits + '!@#$%^&*'
        return ''.join(random.choice(chars) for _ in range(length))
    
    @staticmethod
    def random_date(start_date=None, end_date=None):
        """Генерация случайной даты в формате ДД.ММ.ГГГГ"""
        if not start_date:
            start_date = datetime.now() - timedelta(days=365*5)
        if not end_date:
            end_date = datetime.now()
            
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + timedelta(days=random_number_of_days)
        return random_date.strftime("%d.%m.%Y")


class DataResetPage:
    """Данные для тестирования сброса пароля"""
    
    @property
    def email(self):
        return DataGenerator.random_email()
    
    @property
    def expired_token(self):
        """Генерация истекшего токена (пример)"""
        return f"expired_token_{DataGenerator.random_string(16)}_exp"


class UserData:
    """Данные пользователя с динамической генерацией"""
    
    def __init__(self):
        self._email = DataGenerator.random_email('yandex.ru')
        self._password = DataGenerator.random_password()
    
    @property
    def email(self):
        return self._email
    
    @property
    def user(self):
        return self._email.split('@')[0]
    
    @property
    def password(self):
        return self._password
    
    @property
    def new_password(self):
        """Генерация нового пароля для тестов смены пароля"""
        return f"New{self._password}123!"


user_data = UserData()
