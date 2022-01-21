''' Given a string, check if it is a palindrome or not.
    A palindrome isa word, phrase, or sequence that reads the same backwards as forwards.
    E.g. Ana, Bob, otto, allivessevilla.
'''

# My solution:

my_word = input(f"Write a word to check if it is a palindrome: ").replace(" ", "")

palindrome = my_word[::-1]

if my_word.lower() == palindrome.lower():
    print("Is palindrome.")
else:
    print("Not a palindrome.")