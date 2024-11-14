'''
Write a function that takes a list of numbers and returns a list with the same number of elements, but with each element's value being the running total from the original list.

ex;
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

input: list of int
output: list of running total

1 total 
create new list, running total
if empty return self
else add first  element in list.
go to next item in list and add to total
append to running total list
return list
'''

def running_total(nums):
  running_totals = []
  
  if not nums:
    return nums
  else:
    total = 0
    for num in nums:
      total += num
      running_totals.append(total)
      
  return running_totals

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True