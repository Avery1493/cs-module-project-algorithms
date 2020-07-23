'''
Input: a List of integers
Returns: a List of integers
'''
# def moving_zeroes(arr):
#     # Plan
#     # Count zeros in arr
#     count = arr.count(0)
#     # remove zeros from arr
#     while 0 in arr:
#         arr.remove(0)
#     # if zero >= 1:
#     while count > 0:
#         # append zero * count to end of arr
#         arr.append(0)
#         count -= 1
#     # return arr
#     return arr


def moving_zeroes(arr):
    # initialize a left and right pointer
    # left is 0
    left = 0
    # right is last in arr
    right = len(arr) -1

    # while left <=right
    while left <= right:
        # if left points at 0 and right points at non-zero
        if arr[left] == 0 and arr[right] != 0:
            # swap
            arr[left], arr[right] = arr[right], arr[left]
            # increment left
            left += 1
            # decrement right
            right -= 1
        # else 
        else:
            # if left is non-zero
            if arr[left] != 0:
                # increment left
                left += 1
            # if right is zero
            if arr[right] == 0:
                #decrement right
                right -= 1
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    #arr = [0, 3, 1, 0, -2]
    arr = [1, 2, 3, 0, 4, 0, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")


    # selection or bubble sort
        #understand and can write
    # comfortable with recursion
        # all instances of st
    # time complexty of code
        # binary search O(logn) - halfing 
        # recognize when binary search is important to use
        # array sorted, looking for item