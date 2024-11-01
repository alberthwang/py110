
def getNumbers():
  user_input = []
  
  num1 = input('Enter the 1st number: ')
  num2 = input('Enter the 2nd number: ')
  num3 = input('Enter the 3rd number: ')
  num4 = input('Enter the 4th number: ')
  num5 = input('Enter the 5th number: ')
  
  user_input.append(num1)
  user_input.append(num2)
  user_input.append(num3)
  user_input.append(num4)
  user_input.append(num5)
  
  num6 = input('Enter the last number: ')
  
  formatted_input = ' '.join(user_input)
  
  if num6 in user_input:
    print(f'{num6} is in {formatted_input}')
  else:
    print(f"{num6} isn't in {formatted_input}")

def run():
  getNumbers()

run()