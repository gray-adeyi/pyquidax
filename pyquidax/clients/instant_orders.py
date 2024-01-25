from typing import Literal, Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import (
    CurrencyPair,
    OrderState,
    append_query_parameters,
    HTTPMethod,
    Currency,
    OrderType,
)


class InstantOrderClient(BaseAPIWrapper):
    """A wrapper that enables authenticated
    users to buy and sell cryptocurrencies at the current market price.
    """

    def all(
        self,
        pair: Optional[CurrencyPair] = None,
        state: Optional[OrderState] = None,
        order_by: Literal["asc", "desc"] = "asc",
        user_id: str = "me",
    ):
        """Fetches all instant orders, that have previously executed by you or your authenticated users.

        Args:
            pair: CurrencyPair.BTN_USDT, CurrencyPair.LTC_NGN etc.
            state: OrderState.DONE, OrderState.CONFIRM, OrderState.CANCEL, OrderState.WAIT.
                Defaults to done if not specified.
            order_by: The Order in which you  retrieve result either ascending or descending order
            user_id: The User ID. Use 'me'
            if fetching wallets of main authenticated user, use the user_id if fetching
                for Sub-account linked to the authenticated user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        query_params = (("market", pair), ("state", state), ("order_by", order_by))
        url = append_query_parameters(
            f"{self.base_url}/users/{user_id}/instant_orders", query_params
        )
        return self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )

    def get(self, id: str, user_id: str = "me"):
        """Fetch detail of an instant order

        Args:
            id: This is the unique id used to identify instant orders.
            user_id: The User ID. Use 'me' for the main authenticated user,
                use the user_id if fetching for Subaccount linked to the authenticated user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """

        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/instant_orders/{id}",
            method=HTTPMethod.GET,
        )

    def create(
        self,
        bid: Currency,
        ask: Currency,
        type: OrderType,
        volume: int,
        unit: int,
        user_id: str = "me",
    ):
        """Create Instant Order

        Args:
            bid: Currency.BITCON. Currency.NAIRA etc.
            ask: Currency.BINANCE_COIN, Currency.PANCAKE_SWAP etc.
            type: OrderType.BUY or OrderType.SELL
            volume: Used if unit is in bid currency.
            unit: The unit in which the order will be estimated,
                The unit in which the order will be estimated.
            user_id:  The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Subaccount linked to the authenticated user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        data = {
            "bid": bid,
            "ask": ask,
            "type": type,
            "volume": volume,
            "unit": unit,
        }
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/instant_orders",
            method=HTTPMethod.POST,
            data=data,
        )

    def confirm(self, id: str, user_id: str = "me"):
        """Confirmation of an instant order enqueues the order for final execution.

        Args:
            id:iD of an instant order
            user_id: The User ID. Use 'me' for the main authenticated user,
                use the user_id if fetching for Subaccount linked to the authenticated user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/instant_orders/{id}/confirm",
            method=HTTPMethod.POST,
        )

    def requote(self, id: str, user_id: str = "me"):
        """Requote an Instant Order

                Args:
                    id:iD of an instant order
                    user_id: The User ID. Use 'me' for the main authenticated user,
                        use the user_id if fetching for Subaccount linked to the authenticated user.
        :

                Returns:
                    APIResponse, which is a dataclass containing the response gotten from Quidax servers.
                    `APIResponse.status_code` (int) is the http status code of the response.
                    `APIResponse.status` (str | None) is the status of the response.
                    `APIResponse.message` (str | None) is the message of the response.
                    `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
                    request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/instant_orders/{id}/requote",
            method=HTTPMethod.POST,
        )


class AsyncInstantOrderClient(BaseAsyncAPIWrapper):
    """An async wrapper that enables authenticated
    users to buy and sell cryptocurrencies at the current market price.
    """

    async def all(
        self,
        pair: Optional[CurrencyPair] = None,
        state: Optional[OrderState] = None,
        order_by: Literal["asc", "desc"] = "asc",
        user_id: str = "me",
    ):
        """Fetches all instant orders, that have previously executed by you or your authenticated users.

        Args:
            pair: CurrencyPair.BTN_USDT, CurrencyPair.LTC_NGN etc.
            state: OrderState.DONE, OrderState.CONFIRM, OrderState.CANCEL, OrderState.WAIT.
                Defaults to done if not specified.
            order_by: The Order in which you retrieve a result either ascending or descending order
            user_id: The User ID. Use 'me' if fetching wallets of the main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        query_params = (("market", pair), ("state", state), ("order_by", order_by))
        url = append_query_parameters(
            f"{self.base_url}/users/{user_id}/instant_orders", query_params
        )
        return await self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )

    async def get(self, id: str, user_id: str = "me"):
        """Fetch detail of an instant order

        Args:
            id: This is the unique id used to identify instant orders.
            user_id: The User ID. Use 'me' for the main authenticated user,
                use the user_id if fetching for Subaccount linked to the authenticated user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """

        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/instant_orders/{id}",
            method=HTTPMethod.GET,
        )

    async def create(
        self,
        bid: Currency,
        ask: Currency,
        type: OrderType,
        volume: int,
        unit: int,
        user_id: str = "me",
    ):
        """Create Instant Order

        Args:
            bid: Currency.BITCON. Currency.NAIRA etc.
            ask: Currency.BINANCE_COIN, Currency.PANCAKE_SWAP etc.
            type: OrderType.BUY or OrderType.SELL
            volume: Used if unit is in bid currency.
            unit: The unit in which the order will be estimated,
                The unit in which the order will be estimated.
            user_id:  The User ID. Use 'me' if fetching wallets of the main authenticated user,
                use the user_id if fetching for Subaccount linked to the authenticated user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        data = {
            "bid": bid,
            "ask": ask,
            "type": type,
            "volume": volume,
            "unit": unit,
        }
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/instant_orders",
            method=HTTPMethod.POST,
            data=data,
        )

    async def confirm(self, id: str, user_id: str = "me"):
        """Confirmation of an instant order enqueues the order for final execution.

        Args:
            id:iD of an instant order
            user_id: The User ID. Use 'me' for the main authenticated user,
                use the user_id if fetching for Subaccount linked to the authenticated user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """

        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/instant_orders/{id}/confirm",
            method=HTTPMethod.POST,
        )

    async def requote(self, id: str, user_id: str = "me"):
        """Requote an Instant Order

                Args:
                    id:iD of an instant order
                    user_id: The User ID. Use 'me' for the main authenticated user,
                        use the user_id if fetching for Subaccount linked to the authenticated user.
        :

                Returns:
                    APIResponse, which is a dataclass containing the response gotten from Quidax servers.
                    `APIResponse.status_code` (int) is the http status code of the response.
                    `APIResponse.status` (str | None) is the status of the response.
                    `APIResponse.message` (str | None) is the message of the response.
                    `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
                    request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/instant_orders/{id}/requote",
            method=HTTPMethod.POST,
        )
