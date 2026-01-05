from pages.login_page import LoginPage
from pages.main_page import MainPage

from tests.utils.api_helpers import ApiUser, create_api_user


def authorize_new_user(main_page: MainPage, login_page: LoginPage) -> ApiUser:
    user = create_api_user()
    main_page.click_login_btn()
    login_page.login_with_credentials(user.email, user.password)
    return user


def place_order(main_page: MainPage) -> None:
    main_page.add_ingredient_to_order()
    main_page.place_order()
    main_page.close_check_popup()
