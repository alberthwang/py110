'''
alindromic Strings (Part 2)

Write another function that returns True if the string passed as an argument is a palindrome, or False otherwise. 
This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters.
If you wish, you may simplify things by calling the is_palindrome function you wrote in the previous exercise.


input :str
output:bool

need to be case in sens, ignore white space/punc,non alphanum, 
remake string of elgible characters, check string
'''

def is_real_palindrome(word):
  eligible_word = ''
  for letter in word:
    if letter.isalnum():
      eligible_word += letter.lower()  
    
  return True if eligible_word == eligible_word[::-1] else False

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True