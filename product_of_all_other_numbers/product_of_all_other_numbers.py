'''
Input: a List of integers
Returns: a List of integers
'''
import math
def product_of_all_other_numbers(arr):
    # Plan
    # dont override list
    copy = arr.copy()
    index = 0
    # loop through each index
    for num in arr:
        # isolate item from list
        # [map exp] for <name> in <seq exp> if <filter exp>
        prod = [num for num in arr if num != arr[index]]      
        # replace value at index with product of other indexes
        copy[index] = math.prod(prod)
        # increase index
        index += 1
    # return arr
    return copy


if __name__ == '__main__':
    # Use the main function to test your implementation
    #arr = [1, 2, 3, 4, 5]
    arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
