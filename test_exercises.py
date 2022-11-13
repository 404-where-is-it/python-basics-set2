from exercises import *

import os
import pytest
import random

try:
    from math import gcd
except:
   from fractions import gcd

def test_reversed_list():
    for _ in range(5):
        n_b = random.randint(-50, 0)    
        n_e = random.randint(0, 50)
        n = random.randint(1, 10)
        nums = [random.randint(n_b, n_e) for i in range(n)]

        result = reversed_list(nums)
        nums.reverse()

        assert isinstance(result, list)
        assert len(result) == len(nums)
        assert result == nums

def test_prime_true():
    prime_numbers = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
        31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
        73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
        127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
        179, 181, 191, 193, 197, 199,
    ]
    for num in prime_numbers:
        assert prime_number(num)

def test_prime_squares():
    square_numbers = [x**2 for x in range(2, 20)]
    for num in square_numbers:
        assert not prime_number(num)

def test_nonprime():
    nonprime_2 = [x*2 for x in range(2, 20)]
    nonprime_3 = [x*3 for x in range(2, 20)]
    nonprime_5 = [x*5 for x in range(2, 20)]
    nonprime_7 = [x*7 for x in range(2, 20)]

    def check_list(l):
        for num in l:
            assert not prime_number(num)

    check_list(nonprime_2)
    check_list(nonprime_3)
    check_list(nonprime_5)
    check_list(nonprime_7)

def test_longest_word():
    sentence = "this sentence is abracadabra"

    result = longest_word(sentence)
    assert isinstance(result, str)
    assert result == "abracadabra"

def test_is_duplicate():
    assert isinstance(is_duplicate([]), bool)

    assert not is_duplicate([])
    assert not is_duplicate([1])
    assert is_duplicate([1, 1, 1])
    assert not is_duplicate([7, 1, 4, 14, (1, 2), 898, -2, 3, -42, "a"])
    assert is_duplicate([7, 3, 1, 4, "a", 14, (1, 2), 898, -2, 3, -42, "a"])

    lst = [7, 3, 1, 4, "a", 14, (1, 2), 898, -2, 3, -42, "a"]
    for _ in range(5):
        mean1 = random.choice(lst)
        mean2 = random.choice(lst)
        assert is_duplicate([mean1, mean2]) == (mean1 == mean2)

def test_number_conversion():
    assert isinstance(number_conversion(10, 10), int)
    assert number_conversion(10, 2) == 2
    assert number_conversion(12, 3) == 5
    assert number_conversion("111", 8) == 73
    assert number_conversion("111", 16) == 273
    assert number_conversion("0xAB", 16) == 171
    assert number_conversion("0b11", 16) == 2833

def test_common_divisor():
    assert isinstance(common_divisor(1, 1), int)
    assert common_divisor(17, 21) == 1
    assert common_divisor(21, 21) == 21
    assert common_divisor(44, 20) == 4

    for _ in range(20):
        n1 = random.randint(1, 200)
        n2 = random.randint(1, 200)
        assert common_divisor(n1, n2) == gcd(n1, n2)

def test_file_overlap():
    name1 = 'tmp1.txt'
    name2 = 'tmp2.txt'
    def check(data1, data2):
        with open(name1, 'w') as f:
            for l in data1:
                f.write(l)
        with open(name2, 'w') as f:
            for l in data2:
                f.write(l)
        try:
            assert file_overlap(name1, name2) == data2
        except:
            os.remove(name1)
            os.remove(name2)
            raise

    check(['a\n'], ['a\n'])
    check(['a\n'], [])
    check(['a\n', 'b\n'], ['a\n'])
    check([], [])
    os.remove(name1)
    os.remove(name2)

def test_sort_modulo():
    lst = [-1, 0, 15, -9, 5, 4, 120]
    assert isinstance(sort_modulo([]), list)
    assert sort_modulo(lst) == [0, -1, 4, 5, -9, 15, 120]
    assert sort_modulo([]) == []

def test_list_to_pow():
    assert isinstance(list_to_pow(1, 1, 1), dict)
    assert list_to_pow(1, 5, 2) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert list_to_pow(-1, 2, 5) == {-1: -1, 0: 0, 1: 1, 2: 32}
    assert list_to_pow(0, 0, 1) == {0: 0}

def test_numbers_sum(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: '')
    assert numbers_sum() == 0

    monkeypatch.setattr('builtins.input', lambda: '-999')
    assert numbers_sum() == -999

    monkeypatch.setattr('builtins.input', lambda: '1, 2, 3, 4, 5')
    assert numbers_sum() == 15

    monkeypatch.setattr('builtins.input', lambda: '-1, -2')
    assert numbers_sum() == -3
