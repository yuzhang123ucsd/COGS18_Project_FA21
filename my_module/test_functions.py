"""
Test for my functions.

Here I only tested the functions that actually make sense to use assert on.
"""

from my_module.functions import find_gcd, find_coprime_based_on_num, find_inverse_a, check_all_capital
##
##

def test_find_gcd():
    assert find_gcd(5, 6) == 1
    assert find_gcd(2, 4) == 2
    assert find_gcd(1, 5) == 1
    assert find_gcd(9, 6) == 3

def test_find_inverse_a():
    coprime = find_coprime_based_on_num(5, 256)
    assert find_inverse_a(coprime, 256) * coprime % 256 == 1

    coprime = find_coprime_based_on_num(11, 256)
    assert find_inverse_a(coprime, 256) * coprime % 256 == 1

    coprime = find_coprime_based_on_num(255, 256)
    assert find_inverse_a(coprime, 256) * coprime % 256 == 1
    

def test_check_all_capital():
    assert check_all_capital("abBd") == False
    assert check_all_capital("aaaa") == False
    assert check_all_capital("ABC") == True
    assert check_all_capital("") == True
    assert check_all_capital("AB12412C") == False
    assert check_all_capital("csf231") == False