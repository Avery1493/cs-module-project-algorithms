'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Plan
    # Count zeros in arr
    count = arr.count(0)
    # remove zeros from arr
    while 0 in arr:
        arr.remove(0)
    # if zero >= 1:
    while count > 0:
        # append zero * count to end of arr
        arr.append(0)
        count -= 1
    # return arr
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")