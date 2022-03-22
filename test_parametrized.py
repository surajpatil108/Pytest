import pytest

@pytest.mark.parametrize("x, y, z", [(10, 20, 200), (30, 40, 200)])
def test_method(x, y, z):
    assert x*y == z


@pytest.mark.parametrize("username, password",
                         [
                             ("Selenium", "WebDriver"),
                             ("Python", "Pytest"),
                             ("SurajBhau", "Rajput")
                         ]
                         )
def test_login(username, password):
    print(username)
    print(password)
