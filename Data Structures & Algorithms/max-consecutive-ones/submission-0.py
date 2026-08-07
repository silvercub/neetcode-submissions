class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = list()
        current_run = 0
        for num in nums:
            if num == 1:
                current_run += 1
            else:
                max_consecutive_ones.append(current_run)
                current_run = 0
        max_consecutive_ones.append(current_run)
        return max(max_consecutive_ones)
        