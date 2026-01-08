from pages.login_page import LoginPage
from pages.main_page import MainPage

from helpers.api_helpers import ApiUser


def authorize_new_user(main_page: MainPage, login_page: LoginPage, user: ApiUser) -> None:
    main_page.click_login_btn()
    login_page.login_with_credentials(user.email, user.password)


def place_order(main_page: MainPage) -> None:
    main_page.add_ingredient_to_order()
    main_page.place_order()
    main_page.close_check_popup()
