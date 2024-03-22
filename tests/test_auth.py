import pytest
from pages.auth_page import AuthPage


@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
        a = AuthPage(browser)
        a.user_login()