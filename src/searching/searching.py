# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if start > end:
        return -1

    else:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        # arr does not change, we just change start and end
        # target does not change
        # end changes if we're tossing out right side of array
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        
        # start changes if we're tossing out left side of array
        else:
            return binary_search(arr, target, mid + 1, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    low = 0
    high = len(arr) - 1
    mid = 0

    # if low > high:
    #     return -1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1

        elif arr[mid] > target:
            high = mid - 1

        else:
            return mid
    
    return -1


    # else: 
    #     mid = (low + high) // 2

    #     if target == arr[mid]:
    #         return mid
    #     elif target < arr[mid]:
    #         high = mid+1
    #         return agnostic_binary_search(arr, target)
    #     else:
    #         low = mid-1
    #         return agnostic_binary_search(arr, target)