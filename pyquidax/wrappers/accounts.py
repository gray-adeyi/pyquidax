from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import HTTPMethod


class Account(BaseAPIWrapper):
    """
    A class that represent account and has a BaseAPIWrapper as the object
    """

    def __init__(self, secret_key: Optional[str] = None):
        """
        Initializes a new Account instance

        Args:
            secret_key (Optional[str]): The secret key used for authentication
        """
        super().__init__(secret_key)

    def create_sub_account(
        self, email: str, first_name: str, last_name: str, phone_number: str
    ):
        """
        Creates a sub account

        Args:
            email (str): The email address of the sub account
            first_name (str): The First of the sub account owner
            last_name (str): The last name of the sub account owner

        Returns:
            dict: A dictionary containing information about the  sub account
        """
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
        """
        Fetch information about the main account

        Returns:
            dict: A dictionary containing information about
            the main account
        """
        return self._api_call(url=f"{self.base_url}/users/me", method=HTTPMethod.GET)

    def update_sub_account(
        self, user_id: str, email: str, first_name: str, last_name: str
    ):
        """
        Updates the sub account

        Args:
            user_id (str): Updates the User Identification
            email (str): Updates the email of the account user
            first_name (str): Updates the first name
            last_name (str): Updates the last name

        Returns:
            dict: A dictionary containing information about the updated sub account
        """
        data = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
        }
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}", method=HTTPMethod.PUT, data=data
        )

    def get_sub_account(self, user_id: str):
        """
        Fetch the sub account details

        Args:
            user_id (str): The user Identification

        Returns:
            dict: Information about the sub account in a dictionary form

        """
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}", method=HTTPMethod.GET
        )

    def get_sub_accounts(self):
        """
        Retrieve the list of sub accounts

        Returns:
            list: List of sub accounts and their informations
            in dictionary form
        """
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
