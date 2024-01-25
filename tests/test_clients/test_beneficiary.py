from unittest import TestCase, IsolatedAsyncioTestCase

from tests.utils import CredentialMixin


class BeneficiaryClientTestCase(CredentialMixin, TestCase):
    def test_client_can_retrieve_all_beneficiary(self):
        ...

    def test_client_can_create_beneficiary(self):
        ...

    def test_client_can_retrieve_beneficiary(self):
        ...

    def test_client_can_update_beneficiary(self):
        ...


class AsyncBeneficiaryClientTestCase(CredentialMixin, IsolatedAsyncioTestCase):
    def test_client_can_retrieve_all_beneficiary(self):
        ...

    def test_client_can_create_beneficiary(self):
        ...

    def test_client_can_retrieve_beneficiary(self):
        ...

    def test_client_can_update_beneficiary(self):
        ...
