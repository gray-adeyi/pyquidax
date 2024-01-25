from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import (
    Currency,
    HTTPMethod,
    Kind,
    CurrencyPair,
    append_query_parameters,
)
from pyquidax.clients.accounts import AccountClient, AsyncAccountClient
from pyquidax.clients.beneficiary import BeneficiaryClient, AsyncBeneficiaryClient
from pyquidax.clients.deposits import DepositClient, AsyncDepositClient
from pyquidax.clients.instant_orders import InstantOrderClient, AsyncInstantOrderClient
from pyquidax.clients.markets import MarketClient, AsyncMarketClient
from pyquidax.clients.orders import OrderClient, AsyncOrderClient
from pyquidax.clients.trades import TradeClient, AsyncTradeClient
from pyquidax.clients.wallets import WalletClient, AsyncWalletClient
from pyquidax.clients.withdrawals import WithdrawalClient, AsyncWithdrawalClient


class QuidaxClient(BaseAPIWrapper):
    """This is a synchronous client for interacting with endpoints provided by Quidax.

    It provides attribute bindings and methods that represent every endpoint provided by Quidax.
    E.g. `QuidaxClient.accounts` is a binding to the `Account` client which provides methods for endpoints
    related to accounts on the Quidax platform. It also has methods like `validate_address`
    """

    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)
        self.accounts = AccountClient(secret_key)
        self.beneficiaries = BeneficiaryClient(secret_key)
        self.deposits = DepositClient(secret_key)
        self.instant_orders = InstantOrderClient(secret_key)
        self.markets = MarketClient(secret_key)
        self.orders = OrderClient(secret_key)
        self.trades = TradeClient(secret_key)
        self.wallets = WalletClient(secret_key)
        self.withdrawals = WithdrawalClient(secret_key)

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


class AsyncQuidaxClient(BaseAsyncAPIWrapper):
    """This is an asynchronous client for interacting with endpoints provided by Quidax.

    It provides attribute bindings and methods that represent every endpoint provided by Quidax.
    E.g. `AsyncQuidaxClient.accounts` is a binding to the `Account` client which provides methods for endpoints
    related to accounts on the Quidax platform. It also has methods like `validate_address`
    """

    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)
        self.accounts = AsyncAccountClient(secret_key)
        self.beneficiaries = AsyncBeneficiaryClient(secret_key)
        self.deposits = AsyncDepositClient(secret_key)
        self.instant_orders = AsyncInstantOrderClient(secret_key)
        self.markets = AsyncMarketClient(secret_key)
        self.orders = AsyncOrderClient(secret_key)
        self.trades = AsyncTradeClient(secret_key)
        self.wallets = AsyncWalletClient(secret_key)
        self.withdrawals = AsyncWithdrawalClient(secret_key)

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
