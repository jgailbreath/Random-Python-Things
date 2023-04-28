# Sorting Algorithms
# --Binary Sort--
# An algorithm whose input is a sorted list of elements.
# The search returns the position where a specified element is located, or null if not found.
# Performance: worst case results = log(2) n steps .
# The log of a number is the "flip" of the exponential value of the base number provided, so log(2) 8 = 3, so 2^3 = 8.
# In comparisson, a simple search could take max n steps (known as linear time).
def binary_search(my_list, item):
    low =0
    high=len(my_list)-1
    
    while low<=high:
        mid = (low+high)//2
        check = my_list[mid]
        if check == item:
            return mid
        if check>item:
            high=mid
        else:
            low = mid+1
    return None
values = [1,3,5,7,9,12,32,55,88.101]
print (binary_search(values, 32))
# Question: What would be the max number of steps if the list was 128 integers?  A:7.
# What about if it was double that?  A:8.


