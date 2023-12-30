from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import (
    Currency,
    HTTPMethod,
    Kind,
    CurrencyPair,
    append_query_parameters,
)
from pyquidax.wrappers.accounts import Account
from pyquidax.wrappers.beneficiary import Beneficiary
from pyquidax.wrappers.deposits import Deposit
from pyquidax.wrappers.instant_orders import InstantOrder
from pyquidax.wrappers.markets import Market
from pyquidax.wrappers.orders import Order
from pyquidax.wrappers.trades import Trade
from pyquidax.wrappers.wallets import Wallet
from pyquidax.wrappers.withdrawals import Withdrawal


class Quidax(BaseAPIWrapper):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)
        self.accounts = Account(secret_key)
        self.beneficiaries = Beneficiary(secret_key)
        self.deposits = Deposit(secret_key)
        self.instant_orders = InstantOrder(secret_key)
        self.markets = Market(secret_key)
        self.orders = Order(secret_key)
        self.trades = Trade(secret_key)
        self.wallets = Wallet(secret_key)
        self.withdrawals = Withdrawal(secret_key)

    def validate_address(self, currency: Currency, address: str):
        return self._api_call(
            url=f"{self.base_url}/{currency}/{address}/validate_address",
            method=HTTPMethod.GET,
        )

    def quotes(self, pair: CurrencyPair, unit: Currency, kind: Kind, volume: int):
        query_params = (
            ("market", pair),
            ("unit", unit),
            ("kind", kind),
            ("volume", volume),
        )
        url = append_query_parameters(
            f"{self.base_url}/quotes",
            query_params,
        )
        return self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )

    def withdrawal_fee(self, currency: Currency):
        return self._api_call(
            url=f"{self.base_url}/fee?currency={currency}", method=HTTPMethod.GET
        )


class AsyncQuidax:
    ...


class AsyncQuidax(BaseAsyncAPIWrapper):
    async def validate_address(self, currency: Currency, address: str):
        return await self._api_call(
            url=f"{self.base_url}/{currency}/{address}/validate_address",
            method=HTTPMethod.GET,
        )

    async def quotes(self, pair: CurrencyPair, unit: Currency, kind: Kind, volume: int):
        query_params = (
            ("market", pair),
            ("unit", unit),
            ("kind", kind),
            ("volume", volume),
        )
        url = append_query_parameters(
            f"{self.base_url}/quotes",
            query_params,
        )
        return await self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )

    async def withdrawal_fee(self, currency: Currency):
        return await self._api_call(
            url=f"{self.base_url}/fee?currency={currency}", method=HTTPMethod.GET
        )


class AsyncQuidax:
    ...
