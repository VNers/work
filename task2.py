import calendar

year = 2024
month = 5
print(calendar.month(year, month))


import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
print(heap)
print()


import bisect

my_list = [1, 3, 5, 7, 9]
bisect.insort(my_list, 4)
print(my_list)
print()


from array import array

int_array = array('i', [1, 2, 3, 4, 5])
int_array.append(6)
print(int_array)
print()


from enum import Enum, auto


class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(Color.RED)
print(Color.GREEN)
