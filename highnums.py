def sdd(nums):
  point = 0
  high = 0
  higher = []
  
  for i in range(0, len(nums) - 1):
    high = nums[i]
    point = i+1
    if nums[point] > high:
      higher.append(nums[point])
    else:
      point +=1
      while point < len(nums):
        if high > nums[point]:
          point += 1
        else:
          higher.append(nums[point])
          high = nums[point]
          break
      if high == nums[i]:
        higher.append(-1)
        
  higher.append(-1)
  print(higher)
  return higher
  
  
print(sdd([1, 6, 9, 2, 71]) == [6, 9, 71, 71, -1])
print(sdd([1, 2, 3, 4, 5]) == [2, 3, 4, 5, -1])
print(sdd([5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1])

          