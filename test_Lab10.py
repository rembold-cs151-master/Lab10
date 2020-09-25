# Autotests for Lab 10

import pytest
from Lab10 import is_simple_palindrome, simplify_string

class Test_is_simple_palindrome:
    def test_returns_something(self):
        assert is_simple_palindrome("racecar") is not None

    def test_palindromes_true(self):
        simple_palindromes = ["racecar", "kayak", "rotator", "wow"]
        for word in simple_palindromes:
            assert is_simple_palindrome(word)

    def test_nonpalindromes_false(self):
        simple_words = ["river", "fish", "racecars", "poppy"]
        for word in simple_words:
            assert not is_simple_palindrome(word)

    def test_handles_capitals(self):
        simple_palindromes = ["Racecar", "KayaK", "rotator", "WOW"]
        for word in simple_palindromes:
            assert is_simple_palindrome(word)

class Test_simplify_string:
    def test_returns_something(self):
        assert simplify_string("racecar") is not None

    def test_removes_punctuation(self):
        strings = ["oh-no", "yikes!", "we've"]
        sols = ["ohno", "yikes", "weve"]
        for word, sol in zip(strings, sols):
            assert simplify_string(word) == sol

    def test_removes_whitespace(self):
        strings = ["hello there", " j e d  "]
        sols = ["hellothere", "jed"]
        for word, sol in zip(strings, sols):
            assert simplify_string(word) == sol

    def test_removes_punc_and_whitespace(self):
        strings = ["i'm so happy!", "wait, what happened?" ]
        sols = ["imsohappy", "waitwhathappened"]
        for word, sol in zip(strings, sols):
            assert simplify_string(word) == sol

class Test_combining_both_functions:
    def test_palindromes_true(self):
        palindromes = [
                "Don't nod.",
                "Step on no pets",
                "No lemon, no melon",
                "Eva, can I see bees in a cave?",
                "I did, did I?"
                ]
        for word in palindromes:
            assert is_simple_palindrome(simplify_string(word))

    def test_nonpalindromes_false(self):
        palindromes = [
                "This is not a palindrome!",
                "Suprisingly, this isn't either!",
                "I'm amazed this isn't working.",
                "Why are palindromes so difficult?",
                ]
        for word in palindromes:
            assert not is_simple_palindrome(simplify_string(word))
