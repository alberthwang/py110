'''
Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size.
For instance, the word size of "it's" is 3, not 4.

in: string 0+ chars 
'''

def word_sizes(string):
  frequency = {}
  
  if not string:
    return frequency
  else:
    sentence = string.split(' ')
    
    for word in sentence:
      word_size = 0
      #print(word)
      
      for letter in word:
        if letter.isalpha():
          word_size += 1
      
      if word_size not in frequency:
        frequency[word_size] = 1
      else:
        frequency[word_size] += 1
      #print(frequency)
  
  return frequency

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})