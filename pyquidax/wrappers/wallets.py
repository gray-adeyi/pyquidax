from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import HTTPMethod, Currency, Network


class Wallet(BaseAPIWrapper):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    def main(self):
        return self._api_call(
            url=f"{self.base_url}/users/me/wallets",
            method=HTTPMethod.GET,
        )

    def get(self, user_id: str, currency: Currency):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}",
            method=HTTPMethod.GET,
        )

    def payment_address(self, user_id: str, currency: Currency):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}/address",
            method=HTTPMethod.GET,
        )

    def payment_addresses(self, user_id: str, currency: Currency):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}/addresses",
            method=HTTPMethod.GET,
        )

    def payment_address_by_id(self, user_id: str, currency: Currency, address_id: str):
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}/addresses/{address_id}",
            method=HTTPMethod.GET,
        )

    def create_payment_address(
        self, user_id: str, currency: Currency, network: Optional[Network] = None
    ):
        url = f"{self.base_url}/users/{user_id}/wallets/{currency}/addresses"
        if network:
            url += f"?network={network}"
        return self._api_call(
            url=url,
            method=HTTPMethod.POST,
        )


class AsyncWallet(BaseAsyncAPIWrapper):
    async def main(self):
        return await self._api_call(
            url=f"{self.base_url}/users/me/wallets",
            method=HTTPMethod.GET,
        )

    async def get(self, user_id: str, currency: Currency):
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}",
            method=HTTPMethod.GET,
        )

    async def payment_address(self, user_id: str, currency: Currency):
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}/address",
            method=HTTPMethod.GET,
        )

    async def payment_addresses(self, user_id: str, currency: Currency):
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}/addresses",
            method=HTTPMethod.GET,
        )

    async def payment_address_by_id(
        self, user_id: str, currency: Currency, address_id: str
    ):
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}/addresses/{address_id}",
            method=HTTPMethod.GET,
        )

    async def create_payment_address(
        self, user_id: str, currency: Currency, network: Optional[Network] = None
    ):
        url = f"{self.base_url}/users/{user_id}/wallets/{currency}/addresses"
        if network:
            url += f"?network={network}"
        return await self._api_call(
            url=url,
            method=HTTPMethod.POST,
        )
