from typing import Optional

from pyquidax.base import BaseAPIWrapper
from pyquidax.utils import Currency, HTTPMethod


class Beneficiary(BaseAPIWrapper):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    def all(self, currency: Currency, user_id: str = "me"):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/beneficiaries?currency={currency}",
            method=HTTPMethod.GET,
        )

    def create(self, currency: Currency, uid: str, extra: str, user_id: str = "me"):
        data = {"currency": currency, "uid": uid, "extra": extra}
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/beneficiaries",
            method=HTTPMethod.POST,
            data=data,
        )

    def get(self, id: str, user_id: str = "me"):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/beneficiaries/{id}",
            method=HTTPMethod.GET,
        )

    def update(self, id: str, user_id: str = "me"):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/beneficiaries/{id}",
            method=HTTPMethod.GET,
        )
