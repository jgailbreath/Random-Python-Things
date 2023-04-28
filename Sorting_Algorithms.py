#Sorting Algorithms
#
#Selection Sort
#
#Quicksort
def qsort(arr):
    print ("Quicksort algo working through array:")
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)  // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print (arr)
    return qsort(left) + middle + qsort(right)
test = [6,83,8,3,43,56,1,5,2,7,90]
print ("Test array original is:", test)
print ("Quicksort for test array is: ", qsort(test))

#