import pytest

@pytest.mark.test1
def test_1():           #Pass
    x = 10
    y = 20
    assert 2 * x == y

@pytest.mark.repeat(3)
@pytest.mark.test2
def test_2():           #Fail
    name = "selenium"
    title = "Selenium is for web automation"
    assert name in title

@pytest.mark.test3
def test_3():           #Pass
    name = "Jenkins"
    title = "Jenkins is CI server."
    assert name in title, "Title does not match"

