from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import (
    TransactionState,
    Currency,
    HTTPMethod,
    append_query_parameters,
)


class Deposit(BaseAPIWrapper):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    def all(self):
        return self._api_call(
            url=f"{self.base_url}/users/deposits/all", method=HTTPMethod.GET
        )

    def get_by_user(self, user_id: str, currency: Currency, state: TransactionState):
        query_params = (
            ("currency", currency),
            ("state", state),
        )
        url = append_query_parameters(
            f"{self.base_url}/users/{user_id}/deposits", query_params
        )
        return self._api_call(url=url, method=HTTPMethod.GET)

    def get_by_id(self, deposit_id: str, user_id: str = "me"):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/deposits/{deposit_id}",
            method=HTTPMethod.GET,
        )

class AsyncDeposit(BaseAsyncAPIWrapper):

    async def all(self):
        return await self._api_call(
            url=f"{self.base_url}/users/deposits/all", method=HTTPMethod.GET
        )

    async def get_by_user(self, user_id: str, currency: Currency, state: TransactionState):
        query_params = (
            ("currency", currency),
            ("state", state),
        )
        url = append_query_parameters(
            f"{self.base_url}/users/{user_id}/deposits", query_params
        )
        return await self._api_call(url=url, method=HTTPMethod.GET)

    async def get_by_id(self, deposit_id: str, user_id: str = "me"):
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/deposits/{deposit_id}",
            method=HTTPMethod.GET,
        )
