# Autotests for Lab 8

import pytest
from Lab import is_simple_palindrome, simplify_string, is_sentence_palindrome

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

    # def test_handles_capitals(self):
        # simple_palindromes = ["Racecar", "KayaK", "rotator", "WOW"]
        # for word in simple_palindromes:
            # assert is_simple_palindrome(word)

class Test_simplify_string:
    def test_returns_a_string(self):
        assert type(simplify_string("racecar")) is str

    def test_removes_punctuation(self):
        strings = ["oh-no", "yikes!", "we've", "@#$%^@hi"]
        sols = ["ohno", "yikes", "weve", "hi"]
        for word, sol in zip(strings, sols):
            assert simplify_string(word) == sol

    def test_removes_whitespace(self):
        strings = ["hello there", " j e d  "]
        sols = ["hellothere", "jed"]
        for word, sol in zip(strings, sols):
            assert simplify_string(word) == sol

    def test_lower_capitals(self):
        strings = ["Racecar", "KayaK", "rotator", "WOW"]
        for word in strings:
            assert simplify_string(word) == word.lower()

    def test_combinations_handled(self):
        strings = ["I'm so happy!", "Wait, what just happened?!" ]
        sols = ["imsohappy", "waitwhatjusthappened"]
        for word, sol in zip(strings, sols):
            assert simplify_string(word) == sol

class Test_is_sentence_palindrome:
    def test_palindromes_true(self):
        palindromes = [
                "Don't nod.",
                "Step on no pets",
                "No lemon, no melon",
                "Eva, can I see bees in a cave?",
                "I did, did I?"
                ]
        for word in palindromes:
            assert is_sentence_palindrome(word)

    def test_nonpalindromes_false(self):
        palindromes = [
                "This is not a palindrome!",
                "Suprisingly, this isn't either!",
                "I'm amazed this isn't working.",
                "Why are palindromes so difficult?",
                ]
        for word in palindromes:
            assert not is_sentence_palindrome(word)
