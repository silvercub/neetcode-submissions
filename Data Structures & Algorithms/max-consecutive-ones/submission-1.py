class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0
        current_run = 0
        for num in nums:
            if num == 1:
                current_run += 1
            else:
                if current_run > max_consecutive_ones:
                    max_consecutive_ones = current_run
                current_run = 0
        if current_run > max_consecutive_ones:
            max_consecutive_ones = current_run
        return max_consecutive_ones