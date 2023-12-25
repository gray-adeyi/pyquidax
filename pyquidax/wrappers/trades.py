from typing import Optional

from pyquidax.base import BaseAPIWrapper
from pyquidax.utils import CurrencyPair, HTTPMethod


class Trade(BaseAPIWrapper):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    def all(self, user_id: str):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/trades",
            method=HTTPMethod.GET,
        )

    def get(self, pair: CurrencyPair):
        return self._api_call(
            url=f"{self.base_url}/trades/{pair}",
            method=HTTPMethod.GET,
        )
