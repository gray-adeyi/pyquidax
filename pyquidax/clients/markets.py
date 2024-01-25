from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import HTTPMethod, CurrencyPair, append_query_parameters, Period


class MarketClient(BaseAPIWrapper):
    """A wrapper that enables users to have access to current market-related data"""

    def all(self):
        """List all markets

        The sorting of the list is based on Quidax's internal ranking of the markets

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/markets",
            method=HTTPMethod.GET,
        )

    def tickers(self):
        """List market tickers

        The sorting of the list is based on Quidax's internal ranking of the markets

        Returns:
           APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/markets/tickers",
            method=HTTPMethod.GET,
        )

    def get_ticker(self, pair: CurrencyPair):
        """Fetch a market ticker

        Args:
            pair: CurrencyPair.BTC_USDT, Currencypair.BTC_NGN CurrencyPair.ETH_NGN

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return self._api_call(
            url=f"{self.base_url}/markets/tickers/{pair}",
            method=HTTPMethod.GET,
        )

    def get_k_line(
        self,
        pair: CurrencyPair,
        timestamp: Optional[int] = None,
        period: Optional[Period] = None,
        limit: Optional[int] = None,
    ):
        """Fetch k-line for a market

        Args:
            pair: CurrencyPair.DASH_NGN, CurrencyPair.USDT_GHS etc
            timestamp: An integer represents the seconds elapsed since Unix epoch,
                If set, only k-line data after that time will be returned.
            period: Time period of K line. You can choose between  literal[1, 5, 15...]
            limit: Limit the number of returned data points

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        if limit:
            if limit > 10_000:
                raise ValueError("`limit` cannot be greater than `10_000`")
        query_params = (
            ("timestamp", timestamp),
            ("period", period),
            ("limit", limit),
        )
        url = append_query_parameters(f"{self.base_url}/markets/{pair}/k", query_params)
        return self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )

    def get_k_line_with_pending_trades(
        self,
        pair: CurrencyPair,
        trade_id: str,
        limit: Optional[int] = None,
        period: Optional[Period] = None,
        timestamp: Optional[int] = None,
    ):
        """Fetch k-line data with pending trades for a market

        Args:
            pair: CurrencyPair.BNB_USDT, CurrencyPair.TRX_NGN , CurrencyPair.SAFEMOOD_USDT etc
            trade_id: trade_id
            limit: Limit the number of returned data points. Type: Integer.
            period: Time period of K line. You can choose between Literal[1, 5, 15, 30, 60, 120, 240,
                360, 720, 1440, 4320, 10080]
            timestamp: An integer represents the seconds elapsed since Unix epoch,
                    If set, only k-line data after that time will be returned.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        if limit:
            if limit > 10_000:
                raise ValueError("`limit` cannot be greater than `10_000`")
        query_params = (
            ("timestamp", timestamp),
            ("period", period),
            ("limit", limit),
        )
        url = append_query_parameters(
            f"{self.base_url}/markets/{pair}/k_with_pending_trades/{trade_id}",
            query_params,
        )
        return self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )

    def get_order_book(
        self,
        pair: CurrencyPair,
        ask_limit: Optional[int] = None,
        bids_limit: Optional[int] = None,
    ):
        """Fetch order-book items for a market

        Args:
            pair: CurrencyPair.AAVE_USDT CurrencyPair.CAKE_USDT etc
            ask_limit: Limit the number of returned sell orders.
            bids_limit: Limit the number of returned buy orders.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        if ask_limit:
            if ask_limit > 200:
                raise ValueError("`ask_limit` cannot be greater than `200`")
        if bids_limit:
            if bids_limit > 200:
                raise ValueError("`bids_limit` cannot be greater than `200`")
        query_params = (
            ("ask_limit", ask_limit),
            ("bids_limit", bids_limit),
        )
        url = append_query_parameters(
            f"{self.base_url}/markets/{pair}/order_book",
            query_params,
        )
        return self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )

    def get_depth_data(self, pair: CurrencyPair, limit: Optional[int] = None):
        """Fetch depth data for a market

        Args:
            pair: Currencypair. , CurrencyPair. etc
            limit: Maximum item or data to fetch

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        query_params = (("limit", limit),)
        url = append_query_parameters(
            f"{self.base_url}/markets/{pair}/depth",
            query_params,
        )
        return self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )


class AsyncMarketClient(BaseAsyncAPIWrapper):
    """An async wrapper that enables users to have access to current market-related data"""

    async def all(self):
        """List all markets

        The sorting of the list is based on Quidax's internal ranking of the markets

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/markets",
            method=HTTPMethod.GET,
        )

    async def tickers(self):
        """List market tickers

        The sorting of the list is based on Quidax's internal ranking of the markets

        Returns:
           APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/markets/tickers",
            method=HTTPMethod.GET,
        )

    async def get_ticker(self, pair: CurrencyPair):
        """Fetch a market ticker

        Args:
            pair: CurrencyPair.BTC_USDT, Currencypair.BTC_NGN CurrencyPair.ETH_NGN

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        return await self._api_call(
            url=f"{self.base_url}/markets/tickers/{pair}",
            method=HTTPMethod.GET,
        )

    async def get_k_line(
        self,
        pair: CurrencyPair,
        timestamp: Optional[int] = None,
        period: Optional[Period] = None,
        limit: Optional[int] = None,
    ):
        """Fetch k-line for a market

        Args:
            pair: CurrencyPair.DASH_NGN, CurrencyPair.USDT_GHS etc
            timestamp: An integer represents the seconds elapsed since Unix epoch,
                If set, only k-line data after that time will be returned.
            period: Time period of K line. You can choose between  literal[1, 5, 15...]
            limit: Limit the number of returned data points

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        if limit:
            if limit > 10_000:
                raise ValueError("`limit` cannot be greater than `10_000`")
        query_params = (
            ("timestamp", timestamp),
            ("period", period),
            ("limit", limit),
        )
        url = append_query_parameters(f"{self.base_url}/markets/{pair}/k", query_params)
        return await self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )

    async def get_k_line_with_pending_trades(
        self,
        pair: CurrencyPair,
        trade_id: str,
        limit: Optional[int] = None,
        period: Optional[Period] = None,
        timestamp: Optional[int] = None,
    ):
        """Fetch k-line data with pending trades for a market

        Args:
            pair: CurrencyPair.BNB_USDT, CurrencyPair.TRX_NGN , CurrencyPair.SAFEMOOD_USDT etc
            trade_id: trade_id
            limit: Limit the number of returned data points. Type: Integer.
            period: Time period of K line. You can choose between Literal[1, 5, 15, 30, 60, 120, 240,
                360, 720, 1440, 4320, 10080]
            timestamp: An integer represents the seconds elapsed since Unix epoch,
                    If set, only k-line data after that time will be returned.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        if limit:
            if limit > 10_000:
                raise ValueError("`limit` cannot be greater than `10_000`")
        query_params = (
            ("timestamp", timestamp),
            ("period", period),
            ("limit", limit),
        )
        url = append_query_parameters(
            f"{self.base_url}/markets/{pair}/k_with_pending_trades/{trade_id}",
            query_params,
        )
        return await self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )

    async def get_order_book(
        self,
        pair: CurrencyPair,
        ask_limit: Optional[int] = None,
        bids_limit: Optional[int] = None,
    ):
        """Fetch order-book items for a market

        Args:
            pair: CurrencyPair.AAVE_USDT CurrencyPair.CAKE_USDT etc
            ask_limit: Limit the number of returned sell orders.
            bids_limit: Limit the number of returned buy orders.

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request
        """
        if ask_limit:
            if ask_limit > 200:
                raise ValueError("`ask_limit` cannot be greater than `200`")
        if bids_limit:
            if bids_limit > 200:
                raise ValueError("`bids_limit` cannot be greater than `200`")
        query_params = (
            ("ask_limit", ask_limit),
            ("bids_limit", bids_limit),
        )
        url = append_query_parameters(
            f"{self.base_url}/markets/{pair}/order_book",
            query_params,
        )
        return await self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )

    async def get_depth_data(self, pair: CurrencyPair, limit: Optional[int] = None):
        """Fetch depth data for a market

        Args:
            pair: Currencypair. , CurrencyPair. etc
            limit: Maximum item or data to fetch

        Returns:
            APIResponse, which is a dataclass containing the response gotten from Quidax servers.
            `APIResponse.status_code` (int) is the http status code of the response.
            `APIResponse.status` (str | None) is the status of the response.
            `APIResponse.message` (str | None) is the message of the response.
            `APIResponse.data` (dict | None) is the data returned by Quidax as a result of the
            request sent.
        """
        query_params = (("limit", limit),)
        url = append_query_parameters(
            f"{self.base_url}/markets/{pair}/depth",
            query_params,
        )
        return await self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )
