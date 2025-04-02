print(ord('a')) #97
print(ord('(')) #40
print('a' > '(') # True 97 > 40

words = ['hi', 'bye', 'salutations']
sorted_words = sorted(words, key=len, reverse=True)
print(sorted_words)

people = [("Albert", 30), ("Jasper", 25), ("Betty", 25), ("Anna", 30)]
sorted_people = sorted(people)
print(sorted_people)
# Expected output: [('Betty', 25), ('Jasper', 25), ('Albert', 30), ('Anna', 30)]
# Actual output:   [('Albert', 30), ('Anna', 30), ('Betty', 25), ('Jasper', 25)]

def person_key(person):
    name, age = person
    return (age, name)

sorted_people = sorted(people, key=person_key)

print(sorted_people)