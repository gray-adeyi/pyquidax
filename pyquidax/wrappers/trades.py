from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import CurrencyPair, HTTPMethod


class Trade(BaseAPIWrapper):
    """A Wrapper that fetch trades for the authenticated user"""

    def all(self, user_id: str):
        """Fetch trades for the authenticated user or a sub account


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
            url=f"{self.base_url}/users/{user_id}/trades",
            method=HTTPMethod.GET,
        )

    def get(self, pair: CurrencyPair):
        """Fetch recent trades for a given market pair

        Args:
            pair: CurrencyPair.LTC_NGN , CurrencyPair.USDT_NGN etc

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/trades/{pair}",
            method=HTTPMethod.GET,
        )


class AsyncTrade(BaseAsyncAPIWrapper):
    async def all(self, user_id: str):
        """Fetch trades for the authenticated user or a sub account


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
            url=f"{self.base_url}/users/{user_id}/trades",
            method=HTTPMethod.GET,
        )

    async def get(self, pair: CurrencyPair):
        """Fetch recent trades for a given market pair

        Args:
            pair: CurrencyPair.LTC_NGN , CurrencyPair.USDT_NGN etc

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/trades/{pair}",
            method=HTTPMethod.GET,
        )
