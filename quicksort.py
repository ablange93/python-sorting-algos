def quicksort(list, start, end):
  # BASE CASE #
  if start >= end:
    return
  
  # Define pivot variable and swap with last element
  pivot_idx = randrange(start, end)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  
  # INDUCTIVE STEP #
  print(list[start])
  start += 1
  quicksort(list, start, end)