import pytest


def test_succeed(strict=True):
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False