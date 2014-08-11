def bubble_sort(array):
  array_length = len(array)
  i = 0
  while i <= (array_length - 1):
    i += 1
    for place in range(array_length - i):
      if array[place] > array[place + 1]:
        array[place], array[place + 1] = array[place + 1], array[place]
  return array

print bubble_sort([3,4,2,1,6,51,3,4,5,3,-12,44,30,11])




