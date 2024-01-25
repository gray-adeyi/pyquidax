from unittest import TestCase, IsolatedAsyncioTestCase

from tests.utils import CredentialMixin


class WalletClientTestCase(CredentialMixin, TestCase):
    def test_client_can_retrieve_main_wallet(self):
        ...

    def test_client_can_retrieve_a_wallet(self):
        ...

    def test_client_can_retrieve_wallet_payment_address(self):
        ...

    def test_client_can_retrieve_wallet_payment_addresses(self):
        ...

    def test_client_can_retrieve_payment_address_by_id(self):
        ...

    def test_client_can_create_payment_address(self):
        ...


class AsyncWalletClientTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    async def test_client_can_retrieve_main_wallet(self):
        ...

    async def test_client_can_retrieve_a_wallet(self):
        ...

    async def test_client_can_retrieve_wallet_payment_address(self):
        ...

    async def test_client_can_retrieve_wallet_payment_addresses(self):
        ...

    async def test_client_can_retrieve_payment_address_by_id(self):
        ...

    def test_client_can_create_payment_address(self):
        ...
