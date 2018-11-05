def quicksort(list, start, end):
  # BASE CASE
  if start >= end:
    return
  
  # INDUCTIVE STEP
  print(list[start])
  start += 1
  quicksort(list, start, end)