from unittest import TestCase, IsolatedAsyncioTestCase

from tests.utils import CredentialMixin


class DepositClientTestCase(CredentialMixin, TestCase):
    def test_client_can_retrieve_all_deposits(self):
        ...

    def test_client_can_retrieve_deposits_by_user(self):
        ...

    def test_client_can_retrieve_deposits_by_id(self):
        ...


class AsyncDepositClientTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    async def test_client_can_retrieve_all_deposits(self):
        ...

    async def test_client_can_retrieve_deposits_by_user(self):
        ...

    async def test_client_can_retrieve_deposits_by_id(self):
        ...
