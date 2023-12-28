from typing import Literal, Optional

from pyquidax.base import BaseAPIWrapper
from pyquidax.utils import (
    HTTPMethod,
    OrderType,
    CurrencyPair,
    TransactionState,
    append_query_parameters,
)


class Order(BaseAPIWrapper):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    def create(
        self,
        pair: CurrencyPair,
        type: OrderType,
        price: int,
        volume: int,
        ord_type: Literal["limit", "market"] = "limit",
        user_id: str = "me",
    ):
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
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/orders/{id}", method=HTTPMethod.GET
        )

    def cancel(self, id: str, user_id: str = "me"):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/orders/{id}/cancel",
            method=HTTPMethod.POST,
        )

