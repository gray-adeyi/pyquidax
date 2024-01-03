from typing import Literal, Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import (
    HTTPMethod,
    OrderType,
    CurrencyPair,
    TransactionState,
    append_query_parameters,
)


class Order(BaseAPIWrapper):
    """A wrapper taht enables authenticated users to post bids (buy orders) and asks (sell orders) bids"""

    def create(
        self,
        pair: CurrencyPair,
        type: OrderType,
        price: int,
        volume: int,
        ord_type: Literal["limit", "market"] = "limit",
        user_id: str = "me",
    ):
        """Create a sell or buy order

        Args:
            pair: CurrenecyPair. XRP_NGN, CurrencyPair.DOGE_USDT etc
            type: OrderType.BUY, OrderType.SELL
            price: The price of the order
            volume: Volume of assets
            ord_type: The Order type either Literal["limit", "market"]
            user_id: The User ID. Use 'me' for main authenticated user,
                use the user_id of Sub-account linked to the authenticated user for performing activity for subaccount.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        data = {
            "market": pair,
            "side": type,
            "ord_type": ord_type,
            "price": price,
            "volume": volume,
        }
        if ord_type == "market":
            data.pop("price")
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/orders",
            method=HTTPMethod.POST,
            data=data,
        )

    def all(
        self,
        pair: CurrencyPair,
        state: TransactionState,
        order_by: Literal["asc", "desc"] = "asc",
        user_id: str = "me",
    ):
        """Fetch all orders tethered to the authenticated user

        Args:
            pair: CurrencyuPair.DASH_USDT, CurrencyPair.AFEN_USDT, CurrencyPair.BLS_USDT etc
            state: TransactionState.CHECKED,TransactionState.REJECTED etc
            order_by: The Order in which you retrieve data either ascending or desending order
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        query_params = (
            ("market", pair),
            ("state", state),
            ("order_by", order_by),
        )
        url = append_query_parameters(
            f"{self.base_url}/users/{user_id}/orders", query_params
        )
        return self._api_call(url=url, method=HTTPMethod.GET)

    def get(self, id: str, user_id: str = "me"):
        """A wrapper that enables

        Args:
            id: An ID for the order to fetch
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
            url=f"{self.base_url}/users/{user_id}/orders/{id}", method=HTTPMethod.GET
        )

    def cancel(self, id: str, user_id: str = "me"):
        """Cancels an order tethered to the authenticated user

        Args:
            id: An ID for the order to fetch
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.


        ReTurns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/orders/{id}/cancel",
            method=HTTPMethod.POST,
        )


class AsyncOrder(BaseAsyncAPIWrapper):
    async def create(
        self,
        pair: CurrencyPair,
        type: OrderType,
        price: int,
        volume: int,
        ord_type: Literal["limit", "market"] = "limit",
        user_id: str = "me",
    ):
        """Create a sell or buy order

        Args:
            pair: CurrenecyPair. XRP_NGN, CurrencyPair.DOGE_USDT etc
            type: OrderType.BUY, OrderType.SELL
            price: The price of the order
            volume: Volume of assets
            ord_type: The Order type either Literal["limit", "market"]
            user_id: The User ID. Use 'me' for main authenticated user,
                use the user_id of Sub-account linked to the authenticated user for performing activity for subaccount.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        data = {
            "market": pair,
            "side": type,
            "ord_type": ord_type,
            "price": price,
            "volume": volume,
        }
        if ord_type == "market":
            data.pop("price")
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/orders",
            method=HTTPMethod.POST,
            data=data,
        )

    async def all(
        self,
        pair: CurrencyPair,
        state: TransactionState,
        order_by: Literal["asc", "desc"] = "asc",
        user_id: str = "me",
    ):
        """Fetch all orders tethered to the authenticated user

        Args:
            pair: CurrencyuPair.DASH_USDT, CurrencyPair.AFEN_USDT, CurrencyPair.BLS_USDT etc
            state: TransactionState.CHECKED,TransactionState.REJECTED etc
            order_by: The Order in which you retrieve data either ascending or desending order
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        query_params = (
            ("market", pair),
            ("state", state),
            ("order_by", order_by),
        )
        url = append_query_parameters(
            f"{self.base_url}/users/{user_id}/orders", query_params
        )
        return await self._api_call(url=url, method=HTTPMethod.GET)

    async def get(self, id: str, user_id: str = "me"):
        """A wrapper that enables

        Args:
            id: An ID for the order to fetch
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
            url=f"{self.base_url}/users/{user_id}/orders/{id}", method=HTTPMethod.GET
        )

    async def cancel(self, id: str, user_id: str = "me"):
        """Cancels an order tethered to the authenticated user

        Args:
            id: An ID for the order to fetch
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
            url=f"{self.base_url}/users/{user_id}/orders/{id}/cancel",
            method=HTTPMethod.POST,
        )
