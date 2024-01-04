from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import Currency, TransactionState, HTTPMethod
from decimal import Decimal


class Withdrawal(BaseAPIWrapper):
    """A wrapper that enables authenticated users to send cryptocurrency to internal or external wallets"""

    def all(self, user_id: str, currency: Currency, state: TransactionState):
        """Fetch all withdrawals related to the authenticated user.

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.TRON, Currency.BITCOIN etc
            state: TransactionState.SUBMITTED, TransactionState.SUBMITTING etc

        Returns:
             APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/withdrawals?currency={currency}&state={state}",
            method=HTTPMethod.GET,
        )

    def get(self, user_id: str, withdrawal_id: str):
        """Fetch a Withdrawal detail

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            withdrawal_id: An ID for the withdrawal to fetch

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/withdrawals/{withdrawal_id}",
            method=HTTPMethod.GET,
        )

    def create(
        self,
        user_id: str,
        currency: Currency,
        amount: Decimal,
        fund_uid: str,
        transaction_note: str,
        narration: str,
        fund_uid2: str,
    ):
        """A wrapper that initiates the withdrawal of an authenticated account.

        Args:
            user_id:
            currency: Currency.BITCOIN, Currency.TETHER  etc
            amount: Value to be sent to the recipient.
            fund_uid: This can be the id of your sub user, or crypto address.
            transaction_note: Notes for the recipient
            narration: Narration for the recipient
            fund_uid2: Destination tag

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        data = {
            "currency": currency,
            "amount": str(amount),
            "fund_uid": fund_uid,
            "transaction_note": transaction_note,
            "narration": narration,
            "fund_uid2": fund_uid2,
        }
        return self._api_call(
            url=f"{self.base_url}/users/{user_id}/withdrawals",
            method=HTTPMethod.POST,
            data=data,
        )

    def cancel(self, withdrawal_id: str):
        """Cancel initiated withdrawal.

        Args:
            withdrawal_id: An ID for the withdrawal to cancel

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/users/me/withdrawals/{withdrawal_id}/cancel",
            method=HTTPMethod.POST,
        )


class AsyncWithdrawal(BaseAsyncAPIWrapper):
    """An Async wrapper that enables authenticated users to send cryptocurrency to internal or external wallets"""

    async def all(self, user_id: str, currency: Currency, state: TransactionState):
        """Fetch all withdrawals related to the authenticated user.

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            currency: Currency.TRON, Currency.BITCOIN etc
            state: TransactionState.SUBMITTED, TransactionState.SUBMITTING etc

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/withdrawals?currency={currency}&state={state}",
            method=HTTPMethod.GET,
        )

    async def get(self, user_id: str, withdrawal_id: str):
        """Fetch a Withdrawal detail

        Args:
            user_id: The User ID. Use 'me' if fetching wallets of main authenticated user,
                use the user_id if fetching for Sub-account linked to the authenticated user.
            withdrawal_id: An ID for the withdrawal to fetch
        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/withdrawals/{withdrawal_id}",
            method=HTTPMethod.GET,
        )

    async def create(
        self,
        user_id: str,
        currency: Currency,
        amount: Decimal,
        fund_uid: str,
        transaction_note: str,
        narration: str,
        fund_uid2: str,
    ):
        """A wrapper that initiates the withdrawal of an authenticated account.

        Args:
            user_id:
            currency: Currency.BITCOIN, Currency.TETHER  etc
            amount: Value to be sent to the recipient.
            fund_uid: This can be the id of your sub user, or crypto address.
            transaction_note: Notes for the recipient
            narration: Narration for the recipient
            fund_uid2: Destination tag

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        data = {
            "currency": currency,
            "amount": str(amount),
            "fund_uid": fund_uid,
            "transaction_note": transaction_note,
            "narration": narration,
            "fund_uid2": fund_uid2,
        }
        return await self._api_call(
            url=f"{self.base_url}/users/{user_id}/withdrawals",
            method=HTTPMethod.POST,
            data=data,
        )

    async def cancel(self, withdrawal_id: str):
        """Cancel initiated withdrawal.

        Args:
            withdrawal_id: An ID for the withdrawal to cancel

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/users/me/withdrawals/{withdrawal_id}/cancel",
            method=HTTPMethod.POST,
        )
