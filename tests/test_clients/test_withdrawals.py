from unittest import TestCase, IsolatedAsyncioTestCase

from tests.utils import CredentialMixin


class WithdrawalClientTestCase(CredentialMixin, TestCase):
    def test_client_can_retrieve_all_withdrawals(self):
        ...

    def test_client_can_retrieve_a_withdrawal(self):
        ...

    def test_client_can_create_a_withdrawal(self):
        ...

    def test_client_can_cancel_a_withdrawal(self):
        ...


class AsyncWithdrawalClientTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    def test_client_can_retrieve_all_withdrawals(self):
        ...

    def test_client_can_retrieve_a_withdrawal(self):
        ...

    def test_client_can_create_a_withdrawal(self):
        ...

    def test_client_can_cancel_a_withdrawal(self):
        ...
