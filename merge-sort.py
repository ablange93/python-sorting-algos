# MERGE_SORT #
# merge_sort() recursively breaks down left and right inputs into smaller pieces. #
############
def merge_sort(items):
  # Return input that has less than 2 elements
  if len(items) <= 1:
    return items
  
  # Split up input
  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]
  
  # Call merge_sort() recursivley on left and right
  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)
  
  # Call merge() helper function to combine these broken down lists
  return merge(left_sorted, right_sorted)

# MERGE #
# merge() helper function combines smaller pieces back into a single sorted list. # 
############
def merge(left, right):
  result = []
  
  # While both left and right contain elements
  while (left and right):
    # Compare first element in both 
    if left[0] < right[0]:
      # if left is smaller, add left to result, remove left
      result.append(left[0])
      left.pop(0)
    else:
      # if left is larger, add right to result, remove right
      result.append(right[0])
      right.pop(0)
  
  # Check both left and right for leftover elements. #
  # Add any leftovers to result. #
  if left:
    result += left
  if right:
    result += right
  
  return result
  
# TESTING #
###########  
unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)


print(ordered_list1)
print(ordered_list2)
print(ordered_list3)