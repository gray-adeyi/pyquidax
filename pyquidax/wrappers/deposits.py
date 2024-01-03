from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import (
    TransactionState,
    Currency,
    HTTPMethod,
    append_query_parameters,
)


class Deposit(BaseAPIWrapper):
    def all(self):
        """Fetch all deposits made by sub-users.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/users/deposits/all", method=HTTPMethod.GET
        )

    def get_by_user(self, user_id: str, currency: Currency, state: TransactionState):
        """Fetch deposits by user.

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.ETHEREUM, Currency.BITCOIN_CASH etc
            state: TransactionState.DONE. TransactionState.CHECKED, Transaction.PROCESSING etc

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        query_params = (
            ("currency", currency),
            ("state", state),
        )
        url = append_query_parameters(
            f"{self.base_url}/users/{user_id}/deposits", query_params
        )
        return self._api_call(url=url, method=HTTPMethod.GET)

    def get_by_id(self, deposit_id: str, user_id: str = "me"):
        """Fetch a Deposit

        Args:
            deposit_id: An ID for the deposit to fetch
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
            url=f"{self.base_url}/users/{user_id}/deposits/{deposit_id}",
            method=HTTPMethod.GET,
        )


class AsyncDeposit(BaseAsyncAPIWrapper):
    async def all(self):
        """Fetch all deposits made by sub-users.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """

        return await self._api_call(
            url=f"{self.base_url}/users/deposits/all", method=HTTPMethod.GET
        )

    async def get_by_user(
        self, user_id: str, currency: Currency, state: TransactionState
    ):
        """Fetch deposits by user.

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.ETHEREUM, Currency.BITCOIN_CASH etc
            state: TransactionState.DONE. TransactionState.CHECKED, Transaction.PROCESSING etc

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """

        query_params = (
            ("currency", currency),
            ("state", state),
        )
        url = append_query_parameters(
            f"{self.base_url}/users/{user_id}/deposits", query_params
        )
        return await self._api_call(url=url, method=HTTPMethod.GET)

    async def get_by_id(self, deposit_id: str, user_id: str = "me"):
        """Fetch a Deposit

        Args:
            deposit_id: An ID for the deposit to fetch
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
            url=f"{self.base_url}/users/{user_id}/deposits/{deposit_id}",
            method=HTTPMethod.GET,
        )
