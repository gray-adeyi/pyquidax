from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import Currency, TransactionState, HTTPMethod
from decimal import Decimal


class Withdrawal(BaseAPIWrapper):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    def all(self, user_id: str, currency: Currency, state: TransactionState):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/withdrawals?currency={currency}&state={state}",
            method=HTTPMethod.GET,
        )

    def get(self, user_id: str, withdrawal_id: str):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/withdrawals/{withdrawal_id}",
            method=HTTPMethod.GET,
        )

    def create(
        self,
        user_id: str,
        currency: Currency,
        amount: Decimal,
        fund_uid: str,
        transaction_note: str,
        narration: str,
        fund_uid2: str,
    ):
        data = {
            "currency": currency,
            "amount": str(amount),
            "fund_uid": fund_uid,
            "transaction_note": transaction_note,
            "narration": narration,
            "fund_uid2": fund_uid2,
        }
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/withdrawals",
            method=HTTPMethod.POST,
            data=data,
        )

    def cancel(self, withdrawal_id: str):
        return self._api_call(
            url=f"{self.base_url}/users/me/withdrawals/{withdrawal_id}/cancel",
            method=HTTPMethod.POST,
        )


class AsyncWithdrawal(BaseAsyncAPIWrapper):
    async def all(self, user_id: str, currency: Currency, state: TransactionState):
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/withdrawals?currency={currency}&state={state}",
            method=HTTPMethod.GET,
        )

    async def get(self, user_id: str, withdrawal_id: str):
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/withdrawals/{withdrawal_id}",
            method=HTTPMethod.GET,
        )

    async def create(
        self,
        user_id: str,
        currency: Currency,
        amount: Decimal,
        fund_uid: str,
        transaction_note: str,
        narration: str,
        fund_uid2: str,
    ):
        data = {
            "currency": currency,
            "amount": str(amount),
            "fund_uid": fund_uid,
            "transaction_note": transaction_note,
            "narration": narration,
            "fund_uid2": fund_uid2,
        }
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/withdrawals",
            method=HTTPMethod.POST,
            data=data,
        )

    async def cancel(self, withdrawal_id: str):
        return await self._api_call(
            url=f"{self.base_url}/users/me/withdrawals/{withdrawal_id}/cancel",
            method=HTTPMethod.POST,
        )
