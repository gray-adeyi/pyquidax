import os
from abc import ABC, abstractmethod
from typing import Optional, Union

__version__ = "0.1.0"
__author__ = "Gbenga <adeyigbenga005@gmail.com>"

import httpx

from pyquidax.exceptions import (
    UnsupportedHTTPMethodException,
    ConnectionException,
    MissingSecretKeyException,
)
from pyquidax.utils import HTTPMethod, APIResponse


class AbstractAPIWrapper(ABC):
    ENV_SECRET_KEY_NAME = "QUIDAX_SECRET_KEY"
    API_VERSION = "v1"

    def __init__(self, secret_key: Optional[str] = None):
        self._token = secret_key
        if not self._token:
            self._token = os.environ.get(self.ENV_SECRET_KEY_NAME)
        if not self._token:
            raise MissingSecretKeyException(
                "No secret key was provided! You can provide your Quidax secret key on instantiation "
                f"or as an environmental variable {self.ENV_SECRET_KEY_NAME}=<your-quidax-secret-key>"
            )

    @property
    def base_url(self) -> str:
        return f"https://www.quidax.com/api/{self.API_VERSION}"

    @property
    def headers(self):
        return {
            "authorization": f"Bearer {self._token}",
            "accept": "application/json; charset=utf-8",
            "user-agent": f"PyQuidax {__version__}",
        }

    @abstractmethod
    def _api_call(
        self,
        url: str,
        method: HTTPMethod,
        data: Optional[Union[list, dict]] = None,
    ) -> APIResponse:
        ...

    def _parse_call_kwargs(
        self,
        url: str,
        method: HTTPMethod,
        data: Optional[Union[list, dict]] = None,
    ) -> dict:
        http_method_call_kwargs = {
            "url": url,
            "json": data,
            "headers": self.headers,
        }
        if method in {HTTPMethod.GET, HTTPMethod.DELETE}:
            http_method_call_kwargs.pop("json", None)
        return http_method_call_kwargs

    def _parse_response(self, response: httpx.Response) -> APIResponse:
        response_body = response.json()
        return APIResponse(
            status_code=response.status_code,
            status=str(response_body.get("status")),
            message=response_body.get("message"),
            data=response_body.get("data"),
        )


class BaseAPIWrapper(AbstractAPIWrapper):
    def __init__(self, secret_key: Optional[str] = None):
        """
        Args:
            secret_key: Your Quidax secret key.
        """
        super().__init__(secret_key)

    def _api_call(
        self,
        url: str,
        method: HTTPMethod,
        data: Optional[Union[list, dict]] = None,
    ) -> APIResponse:
        http_method_call_kwargs = self._parse_call_kwargs(
            url=url,
            method=method,
            data=data,
        )
        http_methods_mapping = {
            HTTPMethod.GET: httpx.get,
            HTTPMethod.POST: httpx.post,
            HTTPMethod.PUT: httpx.put,
            HTTPMethod.PATCH: httpx.patch,
            HTTPMethod.DELETE: httpx.delete,
            HTTPMethod.OPTIONS: httpx.options,
            HTTPMethod.HEAD: httpx.head,
        }
        http_method_callable = http_methods_mapping.get(method)
        if not http_method_callable:
            raise UnsupportedHTTPMethodException(
                f"{method} is not a supported HTTP method"
            )
        try:
            response = http_method_callable(**http_method_call_kwargs)
        except httpx.ConnectError:
            raise ConnectionException(
                "Unable to connect to server. Please ensure you have an internet connection"
            )
        except httpx.ConnectTimeout:
            raise ConnectionException("Server refused to respond")
        return self._parse_response(response)


class BaseAsyncAPIWrapper(AbstractAPIWrapper):
    def __init__(self, secret_key: Optional[str] = None):
        super().__init__(secret_key)

    async def _api_call(
        self,
        url: str,
        method: HTTPMethod,
        data: Optional[Union[list, dict]] = None,
    ) -> APIResponse:
        http_method_call_kwargs = self._parse_call_kwargs(
            url=url,
            method=method,
            data=data,
        )
        async with httpx.AsyncClient() as client:
            http_method_callable = getattr(client, method.value.lower(), None)
            if not http_method_callable:
                raise UnsupportedHTTPMethodException(
                    f"{method} is not a supported HTTP method"
                )
            try:
                response = await http_method_callable(**http_method_call_kwargs)
            except httpx.ConnectError:
                raise ConnectionException(
                    "Unable to connect to server. Please ensure you have an internet connection"
                )
            except httpx.ConnectTimeout:
                raise ConnectionException("Server refused to respond")
            return self._parse_response(response)
