from unittest import TestCase, IsolatedAsyncioTestCase

from httpx import codes

from pyquidax.clients.accounts import AccountClient, AsyncAccountClient
from pyquidax.clients.beneficiary import BeneficiaryClient, AsyncBeneficiaryClient
from pyquidax.clients.deposits import DepositClient, AsyncDepositClient
from pyquidax.clients.instant_orders import InstantOrderClient, AsyncInstantOrderClient
from pyquidax.clients.markets import MarketClient, AsyncMarketClient
from pyquidax.clients.orders import OrderClient, AsyncOrderClient
from pyquidax.clients.trades import TradeClient, AsyncTradeClient
from pyquidax.clients.wallets import WalletClient, AsyncWalletClient
from pyquidax.clients.withdrawals import WithdrawalClient, AsyncWithdrawalClient
from pyquidax.quidax import QuidaxClient, AsyncQuidaxClient
from pyquidax.utils import Currency
from tests.utils import CredentialMixin


class QuidaxClientTestCase(CredentialMixin, TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.client = QuidaxClient(cls.secret_key)

    def test_client_has_other_client_bindings(self):
        self.assertTrue(hasattr(self.client, "accounts"))
        self.assertTrue(isinstance(self.client.accounts, AccountClient))

        self.assertTrue(hasattr(self.client, "beneficiaries"))
        self.assertTrue(isinstance(self.client.beneficiaries, BeneficiaryClient))

        self.assertTrue(hasattr(self.client, "deposits"))
        self.assertTrue(isinstance(self.client.deposits, DepositClient))

        self.assertTrue(hasattr(self.client, "instant_orders"))
        self.assertTrue(isinstance(self.client.instant_orders, InstantOrderClient))

        self.assertTrue(hasattr(self.client, "markets"))
        self.assertTrue(isinstance(self.client.markets, MarketClient))

        self.assertTrue(hasattr(self.client, "orders"))
        self.assertTrue(isinstance(self.client.orders, OrderClient))

        self.assertTrue(hasattr(self.client, "trades"))
        self.assertTrue(isinstance(self.client.trades, TradeClient))

        self.assertTrue(hasattr(self.client, "wallets"))
        self.assertTrue(isinstance(self.client.wallets, WalletClient))

        self.assertTrue(hasattr(self.client, "withdrawals"))
        self.assertTrue(isinstance(self.client.withdrawals, WithdrawalClient))

    def test_client_can_validate_address(self):
        ...

    def test_client_can_retrieve_quotes(self):
        ...

    def test_client_can_retrieve_withdrawal_fee(self):
        response = self.client.withdrawal_fee(currency=Currency.BITCOIN)
        self.assertEqual(response.status_code, codes.OK)
        self.assertEqual(response.message, "Successful")


class AsyncQuidaxClientTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.client = AsyncQuidaxClient(cls.secret_key)

    def test_client_has_other_client_bindings(self):
        self.assertTrue(hasattr(self.client, "accounts"))
        self.assertTrue(isinstance(self.client.accounts, AsyncAccountClient))

        self.assertTrue(hasattr(self.client, "beneficiaries"))
        self.assertTrue(isinstance(self.client.beneficiaries, AsyncBeneficiaryClient))

        self.assertTrue(hasattr(self.client, "deposits"))
        self.assertTrue(isinstance(self.client.deposits, AsyncDepositClient))

        self.assertTrue(hasattr(self.client, "instant_orders"))
        self.assertTrue(isinstance(self.client.instant_orders, AsyncInstantOrderClient))

        self.assertTrue(hasattr(self.client, "markets"))
        self.assertTrue(isinstance(self.client.markets, AsyncMarketClient))

        self.assertTrue(hasattr(self.client, "orders"))
        self.assertTrue(isinstance(self.client.orders, AsyncOrderClient))

        self.assertTrue(hasattr(self.client, "trades"))
        self.assertTrue(isinstance(self.client.trades, AsyncTradeClient))

        self.assertTrue(hasattr(self.client, "wallets"))
        self.assertTrue(isinstance(self.client.wallets, AsyncWalletClient))

        self.assertTrue(hasattr(self.client, "withdrawals"))
        self.assertTrue(isinstance(self.client.withdrawals, AsyncWithdrawalClient))

    async def test_client_can_validate_address(self):
        ...

    async def test_client_can_retrieve_quotes(self):
        ...

    async def test_client_can_retrieve_withdrawal_fee(self):
        response = await self.client.withdrawal_fee(currency=Currency.BITCOIN)
        self.assertEqual(response.status_code, codes.OK)
        self.assertEqual(response.message, "Successful")
