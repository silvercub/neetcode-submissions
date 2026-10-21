class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        len_input = len(nums)
        left = 0
        right = len_input - 1
        insert_idx = len_input - 1
        output: List[int] = [0] * len_input
        while insert_idx >= 0:
            left_item = nums[left]
            right_item = nums[right]
            if right_item > abs(left_item):
                output[insert_idx] = right_item ** 2
                right -= 1
            else:
                output[insert_idx] = left_item ** 2
                left += 1
            insert_idx -= 1
        return output



# Trace 1: input list = [-2]
# len_input = 1
# left = 0
# right = 0
# insert_idx = 0
# output = [0]
# loop check is ok, because 0 >= 0
# left_item = -2
# right_item = -2
# -2 is not gt 2
# take else branch and insert -2^2 = 4 at index 0. output is now [4]
# increment left, it is now 1
# decrement insert_idx, it is now -1
# loop check fails because -1 ! ge 0
# exit loop and return output which is 4.


# Trace 2: input list [-1, 0, 1]
# len_input = 3
# left = 0
# right = 3 - 1 = 2
# insert_idx = 3 - 1 = 0
# output is [0, 0, 0]
# loop invariant is satisfied: 2 >= 0
# left_item is -1
# right_item is 1
# if statement is false because right_item(1) ! gt abs(left_item) (1)
# take else branch. square left item and add to list at index 2. list is now [0, 0, 1]
# increment left counter, left is now 1
# decrement insert_idx, insert_idx is now 1
# while condition is satisfied, 1 >= 0
# left_item = 0
# right_item = 1
# right item is gt abs(left_item), 1 > 0
# take if branch, square 1 and add to index 1. list is now [0, 1, 1]
# decrement right, right is now 1
# decrement insert_idx, it is now 0.
# loop condition still holds, 0 >= 0
# left_item = 0
# right item = 0
# condition failed for if, 0 ! gt 0,
# square and insert 0 at index 0. list is now [0, 1, 1]
# decrement insert idx, it is now -1
# loop invariant no longer holds, because -1 ! ge 0
# exit loop and return output, which is [0, 1, 1]. It is ascending.

