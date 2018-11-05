from random import randrange

def quicksort(list, start, end):
  # BASE CASE #
  if start >= end:
    return
  
  # Define pivot variable and swap with last element
  pivot_idx = randrange(start, end)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  
  # Create the lesser_than_pointer
  lesser_than_pointer = start
  # Start a for loop, use 'idx' as the variable
  for idx in range(start, end):
    # Check if the value at idx is less than the pivot
    if list[idx] < pivot_element:
      # Then swap lesser_than_pointer and idx values
      list[lesser_than_pointer], list[idx] = list[idx], list[lesser_than_pointer]
      # increment lesser_than_pointer
      lesser_than_pointer += 1
          
  # Finally swap pivot with value at lesser_than_pointer. #
  list[end], list[lesser_than_pointer] = list[lesser_than_pointer], list[end]
  
  # INDUCTIVE STEP #
  print(list[start])
  start += 1
  quicksort(list, start, end)
  
my_list = [42, 103, 22]
print("BEFORE: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", sorted_list)