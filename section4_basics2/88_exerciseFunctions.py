# Functions Exercise

def highest_even(li: list) -> int:
  highest_even = 0
  for number in li:
    if number % 2 == 0:
      highest_even = number if highest_even < number else highest_even
  return highest_even

print(highest_even([10,2,3,4,8,11,12,24,23,21]))

def highest_evenV2(li: list) -> int:
  while (highest_number := max(li)) % 2 != 0:
    li.remove(highest_number)
  return highest_number

print(highest_evenV2([10,2,3,4,8,11,12,24,23,21]))

def highest_evenV3(li: list) -> int:
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print(highest_evenV3([10,2,3,4,8,11,12,24,23,21]))
