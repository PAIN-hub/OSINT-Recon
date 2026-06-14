from osint.modules import email_breach

def test_email_breach_lookup():
    # Test with a common email address that is likely breached
    res = email_breach.email_breach("test@example.com")
    assert "breaches" in res
    assert isinstance(res["breaches"], list)
    # The return format should have the input email
    assert res["email"] == "test@example.com"

def test_email_breach_clean():
    # Test with an email that shouldn't be found
    res = email_breach.email_breach("clean_email_address_not_breached_12345@domain.com")
    assert "breaches" in res
    assert isinstance(res["breaches"], list)
    assert len(res["breaches"]) == 0
