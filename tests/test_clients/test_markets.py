from unittest import TestCase, IsolatedAsyncioTestCase

from tests.utils import CredentialMixin


class MarketClientTestCase(CredentialMixin, TestCase):
    def test_client_can_retrieve_all_markets(self):
        ...

    def test_client_can_retrieve_tickers(self):
        ...

    def test_client_can_retrieve_a_ticker(self):
        ...

    def test_client_can_retrieve_k_line(self):
        ...

    def test_client_can_retrieve_k_line_with_pending_trades(self):
        ...

    def test_client_can_retrieve_order_book(self):
        ...

    def test_client_can_retrieve_depth_data(self):
        ...


class AsyncMarketClientTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    async def test_client_can_retrieve_all_markets(self):
        ...

    async def test_client_can_retrieve_tickers(self):
        ...

    async def test_client_can_retrieve_a_ticker(self):
        ...

    async def test_client_can_retrieve_k_line(self):
        ...

    async def test_client_can_retrieve_k_line_with_pending_trades(self):
        ...

    async def test_client_can_retrieve_order_book(self):
        ...

    async def test_client_can_retrieve_depth_data(self):
        ...
