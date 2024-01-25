from unittest import TestCase, IsolatedAsyncioTestCase

from tests.utils import CredentialMixin


class InstantOrderClientTestCase(CredentialMixin, TestCase):
    def test_client_can_retrieve_all_instant_orders(self):
        ...

    def test_client_can_retrieve_an_instant_order_by_id(self):
        ...

    def test_client_can_create_an_instant_order(self):
        ...

    def test_client_can_confirm_an_instant_order(self):
        ...

    def test_client_can_requote_an_instant_order(self):
        ...


class AsyncInstantOrderClientTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    async def test_client_can_retrieve_all_instant_orders(self):
        ...

    async def test_client_can_retrieve_an_instant_order_by_id(self):
        ...

    async def test_client_can_create_an_instant_order(self):
        ...

    async def test_client_can_confirm_an_instant_order(self):
        ...

    async def test_client_can_requote_an_instant_order(self):
        ...
