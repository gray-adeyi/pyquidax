from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import Currency, HTTPMethod


class Beneficiary(BaseAPIWrapper):
    """A wrapper for interacting with authenticated user beneficiaries to receive and send assets on Quidax"""

    def all(self, currency: Currency, user_id: str = "me"):
        """Fetch all beneficiaries for the authenticated user or a sub account

        Args:
            currency: Currency Allowed valued: btc, ltc, xrp, dash, trx, doge.

            user_id: the user_id of Sub-account linked to the authenticated user
                for performing actions for a subaccount.

         Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.

        """

        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/beneficiaries?currency={currency}",
            method=HTTPMethod.GET,
        )

    def create(self, currency: Currency, uid: str, extra: str, user_id: str = "me"):
        """Create a beneficiary account for an authenticated account

        Args:
             currency: Currency. Allowed valued: btc, ltc, xrp, dash, trx, doge.
             uid: Wallet Address of your crypto asset.
             extra: Additional defined label for the account.
             user_id: The User ID. Use 'me' for main authenticated user.
             Use the user_id of Sub-account linked to the authenticated user
                for performing actions on a subaccount.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        data = {"currency": currency, "uid": uid, "extra": extra}
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/beneficiaries",
            method=HTTPMethod.POST,
            data=data,
        )

    def get(self, id: str, user_id: str = "me"):
        """Fetches a beneficiary account for an authenticated user.

        Args:
            id: The beneficiary id
            user_id: The User ID. Use 'me' for main authenticated user.
            Use the user_id of Sub-account linked to the authenticated user for performing actions for a subaccount.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/beneficiaries/{id}",
            method=HTTPMethod.GET,
        )

    def update(self, id: str, user_id: str = "me"):
        """Update the beneficiary account.

        Args:
            id: The beneficiary id
            user_id: Use 'me' for main authenticated user ,use the user_id of Sub-account linked
                to the authenticated user for performing actions for a subaccount.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.


        """
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/beneficiaries/{id}",
            method=HTTPMethod.GET,
        )


class AsyncBeneficiary(BaseAsyncAPIWrapper):
    async def all(self, currency: Currency, user_id: str = "me"):
        """Fetch all beneficiaries for the authenticated user or a sub account

        Args:
            currency: Currency Allowed valued: btc, ltc, xrp, dash, trx, doge.

            user_id: the user_id of Sub-account linked to the authenticated user
            for performing actions for a subaccount.

         Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.

        """
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/beneficiaries?currency={currency}",
            method=HTTPMethod.GET,
        )

    async def create(
        self, currency: Currency, uid: str, extra: str, user_id: str = "me"
    ):
        """Create a beneficiary account for an authenticated account

        Args:
             currency: Currency. Allowed valued: btc, ltc, xrp, dash, trx, doge.
             uid: Wallet Address of your crypto asset.
             extra: Additional defined label for the account.
             user_id: The User ID. Use 'me' for main authenticated user.
             Use the user_id of Sub-account linked to the authenticated user for performing actions on a subaccount.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        data = {"currency": currency, "uid": uid, "extra": extra}
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/beneficiaries",
            method=HTTPMethod.POST,
            data=data,
        )

    async def get(self, id: str, user_id: str = "me"):
        """Fetches a beneficiary account for an authenticated user.

        Args:
            id: The beneficiary id
            user_id: The User ID. Use 'me' for main authenticated user.
            use the user_id of Sub-account linked to the authenticated user for performing actions for a subaccount.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/beneficiaries/{id}",
            method=HTTPMethod.GET,
        )

    async def update(self, id: str, user_id: str = "me"):
        """Update the beneficiary account.

        Args:
            id: The beneficiary id
            user_id: Use 'me' for main authenticated user.
            Use the user_id of Sub-account linked to the authenticated user for performing actions for a subaccount.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.


        """
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/beneficiaries/{id}",
            method=HTTPMethod.GET,
        )
