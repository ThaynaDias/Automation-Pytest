import pytest

@pytest.fixture(scope = "function")
def fixtures_function():
    return 10


@pytest.fixture(scope = "module")
def fixtures_module():
    return 20

@pytest.fixture(scope = "session")
def fixture_session():
    return 40


def test_1(fixtures_function):
    assert fixtures_function == 10

def test_2(fixtures_function, fixtures_module):
    assert fixtures_module == 20
    assert fixtures_function == 10

def test_3(fixtures_module,fixture_session):
    assert fixture_session == 40
    assert fixtures_module == 20