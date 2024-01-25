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
    """This is a synchronous client for interacting with endpoints provided by Quidax.

    It provides attribute bindings and methods that represent every endpoint provided by Quidax.
    E.g. `Quidax.accounts` is a binding to the `Account` client which provides methods for endpoints
    related to accounts on the Quidax platform. It also has methods like `validate_address`
    """

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
        """Validates a wallet address.

        Args:
            currency: Any value from the Currency enum matching the currency the wallet supports.
            address: The wallet address to be verified.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/{currency}/{address}/validate_address",
            method=HTTPMethod.GET,
        )

    def quotes(self, market: CurrencyPair, unit: Currency, kind: Kind, volume: int):
        """Retrieves the last current price of an asset.

        Args:
            market: An asset pair of We're interested in retrieving its quote.
            unit: The unit currency of the currency pair.
            kind: Ask or Bid.
            volume: Volume to buy or sell.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        query_params = (
            ("market", market),
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
        """Retrieve the withdrawal fee for a specific currency.

        Args:
            currency: The currency, whose withdrawal fee we want to retrieve.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/fee?currency={currency}", method=HTTPMethod.GET
        )


class AsyncQuidax(BaseAsyncAPIWrapper):
    """This is an asynchronous client for interacting with endpoints provided by Quidax.

    It provides attribute bindings and methods that represent every endpoint provided by Quidax.
    E.g. `Quidax.accounts` is a binding to the `Account` client which provides methods for endpoints
    related to accounts on the Quidax platform. It also has methods like `validate_address`
    """

    async def validate_address(self, currency: Currency, address: str):
        """Validates a wallet address.

        Args:
            currency: Any value from the Currency enum matching the currency the wallet supports.
            address: The wallet address to be verified.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/{currency}/{address}/validate_address",
            method=HTTPMethod.GET,
        )

    async def quotes(
        self, market: CurrencyPair, unit: Currency, kind: Kind, volume: int
    ):
        """Retrieves the last current price of an asset.

        Args:
            market: An asset pair of We're interested in retrieving its quote.
            unit: The unit currency of the currency pair.
            kind: Ask or Bid.
            volume: Volume to buy or sell.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        query_params = (
            ("market", market),
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
        """Retrieve the withdrawal fee for a specific currency.

        Args:
            currency: The currency, whose withdrawal fee we want to retrieve.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/fee?currency={currency}", method=HTTPMethod.GET
        )
