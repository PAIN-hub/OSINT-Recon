from osint.modules import user

def test_username_check():
    res = user.check_username("github")
    assert "results" in res
    assert isinstance(res["results"], dict)