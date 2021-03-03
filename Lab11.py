# File: Lab11.py

"""
Program to check to see if a sentence or phrase
is a palindrome if punctuation, spacing, and
capitalization is ignored.
"""

def is_simple_palindrome(word):
	""" Checks if a single simple word is a palindrome.
	
	Input:
		word (string): the word to check
	Output:
		(bool): if the word is a palindrome
	"""
	pass # Remove once you add your code


def simplify_string(string):
	"""
	Takes a string and removes all non-letter characters. Also
	converts any uppercase characters to lowercase.

	Input:
		string (string): the string to simplify
	Ouput:
		(string): the simplified string
	"""
	pass # Remove once you add your code


def is_sentence_palindrome(sentence):
	"""
	Checks a full complicated sentence to see if it could be
	a sentence palindrome.

	Input:
		sentence (string): the sentence to check
	Ouput:
		(bool): if the sentence is a palindrome
	"""
	pass # Remove once you add your code


if __name__ == "__main__":
    string = input("Enter your desired string: ")
    simple_p = is_simple_palindrome(string)
    print("Is a simple palindrome?", simple_p)

    # Uncomment below block once you have simplify_string up and running
    # simple_string = simplify_string(string)
    # print("The simplified string is:", simple_string)

    # Uncomment below once you have is_sentence_palindrome_running
    # sentence_p = is_sentence_palindrome(string)
    # print("Is a sentence palindrome?", sentence_p)
 
