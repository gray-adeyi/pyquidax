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


class InstantOrder(BaseAPIWrapper):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    def all(
        self,
        pair: Optional[CurrencyPair] = None,
        state: Optional[OrderState] = None,
        order_by: Literal["asc", "desc"] = "asc",
        user_id: str = "me",
    ):
        query_params = (("market", pair), ("state", state), ("order_by", order_by))
        url = append_query_parameters(
            f"{self.base_url}/users/{user_id}/instant_orders", query_params
        )
        return self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )

    def get(self, id: str, user_id: str = "me"):
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
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/instant_orders/{id}/confirm",
            method=HTTPMethod.POST,
        )

    def requote(self, id: str, user_id: str = "me"):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/instant_orders/{id}/requote",
            method=HTTPMethod.POST,
        )


class AsyncInstantOrder(BaseAsyncAPIWrapper):
    async def all(
        self,
        pair: Optional[CurrencyPair] = None,
        state: Optional[OrderState] = None,
        order_by: Literal["asc", "desc"] = "asc",
        user_id: str = "me",
    ):
        query_params = (("market", pair), ("state", state), ("order_by", order_by))
        url = append_query_parameters(
            f"{self.base_url}/users/{user_id}/instant_orders", query_params
        )
        return await self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )

    async def get(self, id: str, user_id: str = "me"):
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
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/instant_orders/{id}/confirm",
            method=HTTPMethod.POST,
        )

    async def requote(self, id: str, user_id: str = "me"):
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/instant_orders/{id}/requote",
            method=HTTPMethod.POST,
        )
