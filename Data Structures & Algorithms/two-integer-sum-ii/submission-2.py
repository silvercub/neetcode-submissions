# basic intuition: we start at both ends with pointers and if the sum of the numbers are greater than the target,
# we decrement the pointer on the right and check again. If the number is smaller than the target  we increment the left pointer and
# check again. This repeats until we left_num + right_num = target or the indexes are equal to each other, meaning we didn't find
# the target.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            left_num = numbers[left]
            right_num = numbers[right]
            num_sum = left_num + right_num
            if num_sum == target:
                return [left + 1, right + 1]
            elif num_sum > target:
                right -= 1
            else:
                left += 1
        return [-1, -1]

# trace 1: [0,1,2,3], target = 5
# left = 0
# right = 4 - 1 = 3
# left < right, 0 < 3, so enter the loop
# left_num = numbers[0] = 0
# right_num = numbers[3] = 3
# num_sum = 0 + 3 = 3
# 3 != 5 so we don't take that branch
# num_sum ! gt target, so don't take else if
# take else branch
# inc left, left now is 1
# left < right, 1 < 3
# left_num = 1
# right_num = 3
# num_sum = 4
# 4 not equal to target of 5
# not gt target of 5
# inc left pointer to 2
# left < right, 2 < 3
# left_num = 2
# right_num = 3
# num_sum = 5
# num_sum == target, so return [2, 3]

# trace 2: [4, 6, 10], target = 10
# left = 0
# right = 3 - 1 = 2
# left < right, so enter loop
# left_num = 4
# right_num = 10
# num_sum = 14
# num_sum not equal target of 10
# num_sum is gt tgt, 14 > 10
# decrement right, right is now 1
# left < right, 0 < 1
# left_num = 4
# right_num = 6
# num_sum = 10
# num_sum == target
# return [0, 1]