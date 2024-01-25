from unittest import TestCase, IsolatedAsyncioTestCase

from tests.utils import (
    MockedAPICallTestCase,
    MockedAsyncAPICallTestCase,
    CredentialMixin,
)


class MockedAccountTestCase(MockedAPICallTestCase):
    def test_can_create_sub_account(self):
        ...

    def test_can_get_main_account(self):
        ...

    def test_can_update_sub_account(self):
        ...

    def test_can_get_sub_account(self):
        ...

    def test_can_get_sub_accounts(self):
        ...


class AccountTestCase(CredentialMixin, TestCase):
    def test_can_create_sub_account(self):
        ...

    def test_can_get_main_account(self):
        ...

    def test_can_update_sub_account(self):
        ...

    def test_can_get_sub_account(self):
        ...

    def test_can_get_sub_accounts(self):
        ...


class MockedAsyncAccountTestCase(MockedAsyncAPICallTestCase):
    async def test_can_create_sub_account(self):
        ...

    async def test_can_get_main_account(self):
        ...

    async def test_can_update_sub_account(self):
        ...

    async def test_can_get_sub_account(self):
        ...

    async def test_can_get_sub_accounts(self):
        ...


class AsyncAccountTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    async def test_can_create_sub_account(self):
        ...

    async def test_can_get_main_account(self):
        ...

    async def test_can_update_sub_account(self):
        ...

    async def test_can_get_sub_account(self):
        ...

    async def test_can_get_sub_accounts(self):
        ...
