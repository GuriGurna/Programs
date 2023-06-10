import ps1

def test_nth_prime():
    assert ps1.nth_prime(1000) == 7919
    assert ps1.nth_prime(500) == 3571
    assert ps1.nth_prime(234) ==1481 
    assert ps1.nth_prime(2345) ==20849
    assert ps1.nth_prime(3) ==5 
    assert ps1.nth_prime(324) ==2143 
    assert ps1.nth_prime(32) == 131
    assert ps1.nth_prime(5) == 11
    assert ps1.nth_prime(86) ==443
    assert ps1.nth_prime(685) ==5119
    assert ps1.nth_prime(566) ==4111
    assert ps1.nth_prime(325) ==2153