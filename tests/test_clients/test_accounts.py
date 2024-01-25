from unittest import TestCase, IsolatedAsyncioTestCase

from tests.utils import (
    CredentialMixin,
)


class AccountClientTestCase(CredentialMixin, TestCase):
    def test_client_can_create_sub_account(self):
        ...

    def test_client_can_retrieve_main_account(self):
        ...

    def test_client_can_update_sub_account(self):
        ...

    def test_client_can_retrieve_sub_account(self):
        ...

    def test_client_can_retrieve_sub_accounts(self):
        ...


class AsyncAccountClientTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    async def test_client_can_create_sub_account(self):
        ...

    async def test_client_can_retrieve_main_account(self):
        ...

    async def test_client_can_update_sub_account(self):
        ...

    async def test_client_can_retrieve_sub_account(self):
        ...

    async def test_client_can_retrieve_sub_accounts(self):
        ...
