from unittest import TestCase, IsolatedAsyncioTestCase

from tests.utils import CredentialMixin


class OrderClientTestCase(CredentialMixin, TestCase):
    def test_client_can_create_order(self):
        ...

    def test_client_can_retrieve_all_orders(self):
        ...

    def test_client_can_retrieve_an_order(self):
        ...

    def test_client_can_cancel_an_order(self):
        ...


class AsyncOrderClientTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    async def test_client_can_create_order(self):
        ...

    async def test_client_can_retrieve_all_orders(self):
        ...

    async def test_client_can_retrieve_an_order(self):
        ...

    async def test_client_can_cancel_an_order(self):
        ...
