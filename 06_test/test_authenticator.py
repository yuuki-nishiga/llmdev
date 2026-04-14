from re import U
import pytest
from authenticator import Authenticator

@pytest.fixture
def authenticator():
    auth = Authenticator()
    yield auth

def test_redister(authenticator):
    authenticator.register("user1", "00000000")
    assert "user1" in authenticator.users

def test_redister_by_value(authenticator, username = "user1", password = "00000000"):
    authenticator.register(username, password)
    with pytest.raises(ValueError, match = "エラー: ユーザーは既に存在します。"):
        authenticator.register(username, password)

def test_login(authenticator, username = "user1", password = "00000000"):
    authenticator.register(username, password)
    result = authenticator.login(username, password)
    assert result == "ログイン成功"

def test_login_by_value(authenticator, username = "user1", password = "00000000", wrongpass = "11111111"):
    authenticator.register(username, password)
    with pytest.raises(ValueError, match = "エラー: ユーザー名またはパスワードが正しくありません。"):
        authenticator.login(username, wrongpass)



