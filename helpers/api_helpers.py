from dataclasses import dataclass
from typing import Any

import requests

from data import DataGenerator, Urls


API_URL = f"{Urls.main_page.rstrip('/')}/api"
AUTH_URL = f"{API_URL}/auth"


@dataclass
class ApiUser:
    email: str
    password: str
    access_token: str


def create_api_user(email_domain: str = "yandex.ru") -> ApiUser:
    payload = {
        "email": DataGenerator.random_email(email_domain),
        "password": DataGenerator.random_password(),
        "name": DataGenerator.random_string(8),
    }
    response = requests.post(f"{AUTH_URL}/register", json=payload, timeout=10)
    response.raise_for_status()
    token = response.json().get("accessToken")
    if not token:
        raise AssertionError("API не вернул accessToken для созданного пользователя")
    return ApiUser(email=payload["email"], password=payload["password"], access_token=token)


def delete_user(user: ApiUser) -> None:
    if not user.access_token:
        return
    try:
        requests.delete(
            f"{AUTH_URL}/user",
            headers={"Authorization": user.access_token},
            timeout=10,
        )
    except requests.RequestException:
        pass


def get_latest_order_number(user: ApiUser) -> str:
    response = requests.get(
        f"{API_URL}/orders",
        headers={"Authorization": user.access_token},
        timeout=10,
    )
    response.raise_for_status()
    orders: list[dict[str, Any]] = response.json().get("orders", [])
    if not orders:
        raise AssertionError("API не вернул заказы пользователя")
    return str(orders[0].get("number"))
