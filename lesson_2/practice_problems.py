#pp1
lst = [10, 9, -6, 11, 7, -16, 50, 8]

print('pp1', sorted(lst))
print(sorted(lst, reverse=True))

#pp2
lst.sort()
print('pp2', lst)
lst.sort(reverse=True)
print(lst)

#pp3, sort list by string with list of int 
lst = [10, 9, -6, 11, 7, -16, 50, 8]

def to_str(word):
    return str(word)
  
lst.sort(key=to_str)
print("pp3",lst)
lst.sort(key=to_str, reverse=True)
print(lst)
#or another more concise way

lst.sort(key=str)
print(lst)

#pp4
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def book_key(book):
  title, author, published = book
  published = int(book['published'])
  return(published, author, title)

org_books = sorted(books, key=book_key)
print(org_books)

#nested data structure
#pp1, get 'g' for all
lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]

lst3 = [['abc'], ['def'], {'third': ['ghi']}]

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}

print(lst1[2][1][3])
print(lst2[1]['third'][0])
print(lst3[2]['third'][0][0])
print(dict1['b'][1])
print(list(dict2['3rd'].keys())[0]) # need to turn keys into list before you can index

#pp2, change 3 to 4
lst1 = [1, [2, 3], 4]

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]

dict1 = {'first': [1, 2, [3]]}

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}

print(lst1)
print(lst2)
print(dict1)
print(dict2)
lst1[1][1] = 4
lst2[2] = 4
dict1['first'][2][0] = 4
dict2['a']['a'][2] = 4

print(lst1)
print(lst2)
print(dict1)
print(dict2)

#pp3
a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a

#a = 4, b = [3,8]
print(a, b) # 2, [3,8], a counts as reassignment so a is unmodified while lst[0] is, b is mutable, actual change to array at the index being made so change is seen.

#pp4
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for mun in munsters:
    print(f'{mun} is a {munsters[mun]['age']}  year old {munsters[mun]['gender']} ')

#other way, cleaner enumerate/unpack
for name, info in munsters.items():
    print(f'{name} is a {info['age']}-year-old {info['gender']}.')
    
    
#pp comprehensions
#1     
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

#for loop
muns = []
for mun in munsters.values():
    if mun['gender'] == 'male':
        muns.append(mun['age'])

print(sum(muns))

#comprehension

mun = [mun['age'] for mun in munsters.values() if mun['gender'] == 'male']
print(mun)
print(sum(mun))

#2
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

for index,element in enumerate(lst):
    lst[index] = sorted(element)

print(lst)

#comprehension
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
lst = [sorted(element) for element in lst]

print(lst)