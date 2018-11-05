from random import randrange, shuffle

def quicksort(list, start, end):
  # BASE CASE #
  if start >= end:
    return
  
  # Define random pivot and swap with last element
  pivot_idx = randrange(start, end)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  
  # create pointer used to track all values lesser than pivot (all go to the left)
  lesser_than_pointer = start
  
  for i in range(start, end):
    # if there's an element out of place
    if list[i] < pivot_element:
      # Then swap element with end of portion of lesser elements
      list[lesser_than_pointer], list[i] = list[i], list[lesser_than_pointer]
      # increment counter so we know we have one more lesser element
      lesser_than_pointer += 1
          
  # move pivot element to the end of portion of lesser elements. 
  list[end], list[lesser_than_pointer] = list[lesser_than_pointer], list[end]
  
  # INDUCTIVE STEP #
  # Recursively call quicksort left & right sub-lists.
  # left sub-list
  quicksort(list, start, lesser_than_pointer - 1)
  # right sub-list
  quicksort(list, lesser_than_pointer + 1, end)
  
### TEST ###  
unsorted_list = [3,7,12,24,36,15,89, 92, 96, 98, 94, 42, 112, 117, 111]
shuffle(unsorted_list)
print(unsorted_list)

# sort list using quicksort() then print
quicksort(unsorted_list, 0, len(unsorted_list) - 1)
print(unsorted_list)