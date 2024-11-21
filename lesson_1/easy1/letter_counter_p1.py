'''
Write a function that takes a string consisting of zero or more space-separated words 
and returns a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

in: string, 0+ chars with space, punct counts as part of word
out: dictionary frequency

separate string by space
create empty dict
loop through list
count the number of chars in word, if num not in dict, add, else +1 to count
return list


'''

def word_sizes(string):
  frequency = {}
  
  if not string:
    return frequency
  else:
    sentence = string.split(' ')
    for word in sentence:
      word_size = len(word)
      #print(word)
      if word_size not in frequency:
        frequency[word_size] = 1
      else:
        frequency[word_size] += 1
      #print(frequency)
  
  return frequency

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})