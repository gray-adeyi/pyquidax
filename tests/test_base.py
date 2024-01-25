from pyquidax.base import BaseAPIWrapper, __version__, BaseAsyncAPIWrapper
from pyquidax.utils import HTTPMethod, APIResponse
from tests.utils import (
    MockedAPICallTestCase,
    MockedAsyncAPICallTestCase,
)


class BaseAPIWrapperTestCase(MockedAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = BaseAPIWrapper(secret_key=cls.secret_key)

    def test_token(self):
        self.assertEqual(self.wrapper._token, self.secret_key)

    def test_headers(self):
        self.assertDictEqual(
            self.wrapper.headers,
            {
                "accept": "application/json; charset=utf-8",
                "authorization": f"Bearer {self.secret_key}",
                "user-agent": f"PyQuidax {__version__}",
            },
        )

    def test__api_call(self):
        response = self.wrapper._api_call(
            url="", method=HTTPMethod.POST, data={"type": "test"}
        )
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(
            response,
            APIResponse(status_code=200, status="None", message=None, data=None),
        )


class BaseAsyncAPIWrapperTestCase(MockedAsyncAPICallTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.wrapper = BaseAsyncAPIWrapper(secret_key=cls.secret_key)

    def test_token(self):
        self.assertEqual(self.wrapper._token, self.secret_key)

    def test_headers(self):
        self.assertDictEqual(
            self.wrapper.headers,
            {
                "accept": "application/json; charset=utf-8",
                "authorization": f"Bearer {self.secret_key}",
                "user-agent": f"PyQuidax {__version__}",
            },
        )

    async def test__api_call(self):
        response = await self.wrapper._api_call(
            url="", method=HTTPMethod.POST, data={"type": "test"}
        )
        self.assertIsInstance(response, APIResponse)
        self.assertEqual(
            response,
            APIResponse(status_code=200, status="None", message=None, data=None),
        )
