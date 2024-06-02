import pytest
from lib.anagram import Anagram

class TestAnagram:
    def test_no_matches(self):
        anagram = Anagram("listen")
        assert anagram.match(['enlists', 'google', 'banana']) == []

    def test_one_match(self):
        anagram = Anagram("listen")
        assert anagram.match(['enlists', 'google', 'inlets', 'banana']) == ['inlets']

    def test_multiple_matches(self):
        anagram = Anagram("listen")
        assert anagram.match(['enlists', 'inlets', 'enlist', 'google', 'banana']) == ['inlets', 'enlist']

    def test_no_input_list(self):
        anagram = Anagram("listen")
        assert anagram.match([]) == []

    def test_case_insensitivity(self):
        anagram = Anagram("Listen")
        assert anagram.match(['enlists', 'Google', 'Inlets', 'banana']) == ['Inlets']
