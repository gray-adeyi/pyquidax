from unittest import TestCase, IsolatedAsyncioTestCase

from tests.utils import CredentialMixin


class TradeClientTestCase(CredentialMixin, TestCase):
    def test_client_can_retrieve_all_trades(self):
        ...

    def test_client_can_retrieve_a_trade(self):
        ...


class AsyncTradeClientTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    async def test_client_can_retrieve_all_trades(self):
        ...

    async def test_client_can_retrieve_a_trade(self):
        ...
