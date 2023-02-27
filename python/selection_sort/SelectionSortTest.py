import random

from selection_sort.SelectionSort import selection_sort

random_numbers = random.sample(range(1, 99999), 100)

sorted = [i for i in range(0, 101)]

reverse = [i for i in range(100, -1, -1)]

repeat = [0,0,0,0,0,3,3,3,1,1,1,1,9,9,10,0,0,0,0,2,2,2,2,33,33,33]

print(selection_sort(random_numbers))
print(selection_sort(sorted))
print(selection_sort(reverse))
print(selection_sort(repeat))
