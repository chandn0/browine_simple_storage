import pytest


@pytest.fixture(scope="module", autouse=True)
def token(SimpleStorage, accounts):
    t = accounts[0].deploy(SimpleStorage)
    yield t


@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass


def test_transfer(token, accounts):
    token.store(100, {"from": accounts[0]})
    assert token.retrieve() == 100


def test_change(token, accounts):
    token.store(200, {"from": accounts[0]})
    assert token.retrieve() == 200
