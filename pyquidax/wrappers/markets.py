from typing import Optional

from pyquidax.base import BaseAPIWrapper, BaseAsyncAPIWrapper
from pyquidax.utils import HTTPMethod, CurrencyPair, append_query_parameters, Period


class Market(BaseAPIWrapper):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    def all(self):
        return self._api_call(
            url=f"{self.base_url}/markets",
            method=HTTPMethod.GET,
        )

    def tickers(self):
        return self._api_call(
            url=f"{self.base_url}/markets/tickers",
            method=HTTPMethod.GET,
        )

    def get_ticker(self, pair: CurrencyPair):
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
        query_params = (("limit", limit),)
        url = append_query_parameters(
            f"{self.base_url}/markets/{pair}/depth",
            query_params,
        )
        return self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )


class AsyncMarket(BaseAsyncAPIWrapper):
    async def all(self):
        return await self._api_call(
            url=f"{self.base_url}/markets",
            method=HTTPMethod.GET,
        )

    async def tickers(self):
        return await self._api_call(
            url=f"{self.base_url}/markets/tickers",
            method=HTTPMethod.GET,
        )

    async def get_ticker(self, pair: CurrencyPair):
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
        query_params = (("limit", limit),)
        url = append_query_parameters(
            f"{self.base_url}/markets/{pair}/depth",
            query_params,
        )
        return await self._api_call(
            url=url,
            method=HTTPMethod.GET,
        )
