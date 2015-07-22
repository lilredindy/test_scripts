

def encode(input_string):
    count = 1
    prev = ''
    lst = []
    character = ''
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    else:
        entry = (character, count)
        lst.append(entry)
    return lst


def decode(lst):
    q = ''
    for character, count in lst:
        q += character * count
    return q


#----------------------------------------------
#----------------------------------------------

import unittest
from hypothesis import given, example, assume
import hypothesis.strategies as st
import math

class TestEncoding(unittest.TestCase):

    @given(st.text())
    @example(s='')
    def test_decode_inverts_encode(self, s):
        assert decode(encode(s)) == s

    @given(st.integers(), st.integers())
    def test_ints_are_commutative(self, x, y):
        assert x + y == y + x

    @unittest.skip("")
    @given(st.integers(), st.integers())
    def test_sqrt(self, x, y):
        assume (x > 50)
        assert math.sqrt(x) == y


    @given(st.lists(st.integers()))
    def test_sum_is_positive(self, xs):
        assume(len(xs) > 3)
        assume(all(x > 0 for x in xs))
        assert sum(xs) > 120
 
if __name__ == '__main__':
    unittest.main()

