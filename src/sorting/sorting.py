# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # creates an aray of 0s that is len(elements)
    merged_arr = [0] * elements
    # merged_arr = [0 for _ in range(elements)] # list comprehension version to accomplish line above

    # Your code here
    a = 0
    b = 0

    for i in range(elements):
        # check if a is in bounds of array a
        if a >= len(arrA):
            # we've moved all the elements from aarA into mergedArr
            # we still have elements from arrB that need to be moved
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
        # check if b is in bounds of array b
            # we've moved all the elements from aarA into mergedArr
            # we still have elements from arrA that need to be moved
            merged_arr[i] = arrA[a]
            a += 1
        # compare arrA[a] against arrB[b]
        elif arrA[a] < arrB[b]:

            #move smaller element into mergedArr
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1  

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        left = merge_sort(arr[0 : len(arr)//2])
        right = merge_sort(arr[len(arr)//2 : ])

        arr = merge(left, right)



    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


# helper function to parition the input array
# def partition(arr):
#     pivot = arr[0]
#     left = []
#     right = []

#     for x in arr[1:]:
#         if x <= pivot:
#             left.append(x)
#         else:
#             right.append(x)
    
#     return left, pivot, right

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr

#     left, picot, right = partition(arr)
#     return quicksort(left) + [pivot] = quicksort(right)

    