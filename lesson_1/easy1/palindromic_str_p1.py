'''

Palindromic Strings (Part 1)

Write a function that returns True if the string passed as an argument is a palindrome, False otherwise.
A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

input: string, case and white space, characters matter
output: bool

'''

def is_palindrome(word):
  return True if word == word[::-1] else False


# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)