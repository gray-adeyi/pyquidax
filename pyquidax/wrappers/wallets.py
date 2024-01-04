from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import HTTPMethod, Currency, Network


class Wallet(BaseAPIWrapper):
    """A Wrapper that creates and manages both fiat and cryptocurrency wallets"""

    def main(self):
        """Fetch all wallets linked to authenticated user or subaccount tethered

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/users/me/wallets",
            method=HTTPMethod.GET,
        )

    def get(self, user_id: str, currency: Currency):
        """Fetch user wallet

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.BINANCE_COIN , Currency.USD_COIN  etc

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}",
            method=HTTPMethod.GET,
        )

    def payment_address(self, user_id: str, currency: Currency):
        """Fetch default payment address for a wallet

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.BINANCE_COIN , Currency.USD_COIN  etc

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}/address",
            method=HTTPMethod.GET,
        )

    def payment_addresses(self, user_id: str, currency: Currency):
        """Fetch Payment Addresses

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.BINANCE_COIN , Currency.USD_COIN  etc

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}/addresses",
            method=HTTPMethod.GET,
        )

    def payment_address_by_id(self, user_id: str, currency: Currency, address_id: str):
        """Fetch details of a payment address, tethered to an authenticated account.

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.BINANCE_COIN , Currency.USD_COIN  etc
            address_id: ID of the payment address to be retrieved

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent
        """
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}/addresses/{address_id}",
            method=HTTPMethod.GET,
        )

    def create_payment_address(
        self, user_id: str, currency: Currency, network: Optional[Network] = None
    ):
        """Create Payment Address for a cryptocurrency

         Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.BINANCE_COIN , Currency.USD_COIN  etc
            network: Network.BTC, Network.BEP20, Network.RIPPLE etc

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent
        """
        url = f"{self.base_url}/users/{user_id}/wallets/{currency}/addresses"
        if network:
            url += f"?network={network}"
        return self._api_call(
            url=url,
            method=HTTPMethod.POST,
        )


class AsyncWallet(BaseAsyncAPIWrapper):
    """An async wrapper that creates and manages both fiat and cryptocurrency wallets"""

    async def main(self):
        """Fetch all wallets linked to authenticated user or subaccount tethered

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/users/me/wallets",
            method=HTTPMethod.GET,
        )

    async def get(self, user_id: str, currency: Currency):
        """Fetch user wallet

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.BINANCE_COIN , Currency.USD_COIN  etc

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}",
            method=HTTPMethod.GET,
        )

    async def payment_address(self, user_id: str, currency: Currency):
        """Fetch default payment address for a wallet

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.BINANCE_COIN , Currency.USD_COIN  etc

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}/address",
            method=HTTPMethod.GET,
        )

    async def payment_addresses(self, user_id: str, currency: Currency):
        """Fetch Payment Addresses

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.BINANCE_COIN , Currency.USD_COIN  etc

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}/addresses",
            method=HTTPMethod.GET,
        )

    async def payment_address_by_id(
        self, user_id: str, currency: Currency, address_id: str
    ):
        """Fetch details of a payment address, tethered to an authenticated account.

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.BINANCE_COIN , Currency.USD_COIN  etc
            address_id: ID of the payment address to be retrieved

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent
        """
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/wallets/{currency}/addresses/{address_id}",
            method=HTTPMethod.GET,
        )

    async def create_payment_address(
        self, user_id: str, currency: Currency, network: Optional[Network] = None
    ):
        """Create Payment Address for a cryptocurrency

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.BINANCE_COIN , Currency.USD_COIN  etc
            network: Network.BTC, Network.BEP20, Network.RIPPLE etc

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent
        """
        url = f"{self.base_url}/users/{user_id}/wallets/{currency}/addresses"
        if network:
            url += f"?network={network}"
        return await self._api_call(
            url=url,
            method=HTTPMethod.POST,
        )
