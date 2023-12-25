from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import HTTPMethod


class Account(BaseAPIWrapper):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    def create_sub_account(
        self, email: str, first_name: str, last_name: str, phone_number: str
    ):
        data = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
        }
        return self._api_call(
            url=f"{self.base_url}/users", method=HTTPMethod.POST, data=data
        )

    def get_main_account(self):
        return self._api_call(url=f"{self.base_url}/users/me", method=HTTPMethod.GET)

    def update_sub_account(
        self, user_id: str, email: str, first_name: str, last_name: str
    ):
        data = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
        }
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}", method=HTTPMethod.PUT, data=data
        )

    def get_sub_account(self, user_id: str):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}", method=HTTPMethod.GET
        )

    def get_sub_accounts(self):
        return self._api_call(url=f"{self.base_url}/users", method=HTTPMethod.GET)


class AsyncAccount(BaseAsyncAPIWrapper):
    async def create_sub_account(
        self, email: str, first_name: str, last_name: str, phone_number: str
    ):
        data = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
        }
        return await self._api_call(
            url=f"{self.base_url}/users", method=HTTPMethod.POST, data=data
        )

    async def get_main_account(self):
        return await self._api_call(
            url=f"{self.base_url}/users/me", method=HTTPMethod.GET
        )

    async def update_sub_account(
        self, user_id: str, email: str, first_name: str, last_name: str
    ):
        data = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
        }
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}", method=HTTPMethod.PUT, data=data
        )

    async def get_sub_account(self, user_id: str):
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}", method=HTTPMethod.GET
        )

    async def get_sub_accounts(self):
        return await self._api_call(url=f"{self.base_url}/users", method=HTTPMethod.GET)
