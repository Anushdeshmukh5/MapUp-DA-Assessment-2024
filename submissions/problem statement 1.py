from typing import List

def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
    i = 0
    
    while i < len(lst):
        start = i
        end = min(i + n - 1, len(lst) - 1) 
        while start < end:
            lst[start], lst[end] = lst[end], lst[start]
            start += 1
            end -= 1
        
        i += n
    
    return lst

print(reverse_by_n_elements([1, 2, 3, 4, 5, 6, 7, 8], 3))  # [3, 2, 1, 6, 5, 4, 8, 7]
print(reverse_by_n_elements([1, 2, 3, 4, 5], 2))           # [2, 1, 4, 3, 5]
print(reverse_by_n_elements([10, 20, 30, 40, 50, 60, 70], 4))  # [40, 30, 20, 10, 70, 60, 50]
