import pytest

@pytest.mark.regression
def test_method2():
    print("Test1")
    assert 1-1 == 2

@pytest.mark.smoke
def test_method3():
    print("Test2")
    assert 1+1 == 2