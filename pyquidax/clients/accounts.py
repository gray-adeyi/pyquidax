from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import HTTPMethod


class AccountClient(BaseAPIWrapper):
    """A wrapper for interacting with user accounts on Quidax"""

    def create_sub_account(
        self, email: str, first_name: str, last_name: str, phone_number: str
    ):
        """Create a subaccount tethered to the authenticated user

        Args:
            email: The email of your sub user, the user email must be unique, and it can't be changed.
            first_name: The first name of your sub user, this field can be edited.
            last_name: The last name of your sub user, this field can be edited.
            phone_number: The user's phone number.

        Returns:
            APIResponse which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
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
        """Fetches the user detail for the parent account.

        This account is a primary account tethered for you to user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(url=f"{self.base_url}/users/me", method=HTTPMethod.GET)

    def update_sub_account(
        self, user_id: str, email: str, first_name: str, last_name: str
    ):
        """Update subaccount information.

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            email: The first name of your sub user, this field can be edited.
            first_name: The email of your sub user, the user email must be unique and it can't be changed.
            last_name: The last name of your sub user, this field can be edited.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
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
        """Get details of a subaccount.

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}", method=HTTPMethod.GET
        )

    def get_sub_accounts(self):
        """Fetch subaccounts tethered to your account.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(url=f"{self.base_url}/users", method=HTTPMethod.GET)


class AsyncAccountClient(BaseAsyncAPIWrapper):
    """An async wrapper for interacting with user accounts on Quidax"""

    async def create_sub_account(
        self, email: str, first_name: str, last_name: str, phone_number: str
    ):
        """Create a subaccount tethered to the authenticated user

        Args:
            email: The email of your sub user, the user email must be unique, and it can't be changed.
            first_name: The first name of your sub user, this field can be edited.
            last_name: The last name of your sub user, this field can be edited.
            phone_number: The user's phone number.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
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
        """Fetches the user detail for the parent account.

        This account is a primary account tethered for you to user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/users/me", method=HTTPMethod.GET
        )

    async def update_sub_account(
        self, user_id: str, email: str, first_name: str, last_name: str
    ):
        """Update subaccount information.

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            email: The first name of your sub user, this field can be edited.
            first_name: The email of your sub user, the user email must be unique and it can't be changed.
            last_name: The last name of your sub user, this field can be edited.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        data = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
        }
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}", method=HTTPMethod.PUT, data=data
        )

    async def get_sub_account(self, user_id: str):
        """Get details of a subaccount.

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}", method=HTTPMethod.GET
        )

    async def get_sub_accounts(self):
        """Fetch subaccounts tethered to your account.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(url=f"{self.base_url}/users", method=HTTPMethod.GET)
