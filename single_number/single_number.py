'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    #Plan
    # loop through arr
    for num in arr: 
        # count each number
        count = arr.count(num)
        # if count == 1
        if count == 1:
            # return number
            return num



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")