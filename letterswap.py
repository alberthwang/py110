'''

Letter Swap

Given a string of words separated by spaces, 
write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. 
You may also assume that each string contains nothing but words and spaces, 
and that there are no leading, trailing, or repeated spaces.

in: string of word can contain number
out string of swapped letter for each word

each letter ,get first letter, last letter, swap, merge all words
return merged string
'''

def swap(sentence):
  words = []
  sentence = sentence.split(' ')
  
  
  for word in sentence:
    print(word)
    swapped_word = word[len(word)-1] + word[1:len(word)-1] + word[0]
    print(swapped_word)
    
print(swap("this is abe abcde"))