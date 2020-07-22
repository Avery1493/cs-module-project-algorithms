'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Plan
    # set start and end
    start = 0
    end = len(nums)
    arr = []
    # while start is less than or equal to end exclusive
    while start <= end - k:
        # slide through list by k
        x = nums[start:start+k]
        # append max to arr
        arr.append(max(x))
        # increase start
        start += 1
    # return arr
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
