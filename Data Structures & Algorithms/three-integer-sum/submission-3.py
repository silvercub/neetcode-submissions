from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output: List[List[int]] = []
        nums.sort()
        prev = None
        for index, num in enumerate(nums):
            a = num
            if index == (len(nums) - 2):
                break
            if a == prev:
                continue # we already compared this number so skip so we don't duplicate
            ref_b = index + 1
            ref_c = len(nums) - 1
            prev_b = None
            prev_c = None
            while (ref_b < ref_c):
                b = nums[ref_b]
                c = nums[ref_c]
                if prev_b == b:
                    ref_b += 1
                    continue
                if prev_c == c:
                    ref_c -= 1
                    continue
                compare_sum = a + b + c
                if compare_sum == 0:
                    output.append([a, b, c])
                    prev_b = b
                    ref_b += 1
                elif compare_sum < 0:
                    ref_b += 1
                    prev_b = b
                else:
                    ref_c -= 1
                    prev_c = c
            prev = a
        return output

# Trace: [-1, 0, 1, 2, -1]
#        output is empty list
#        nums.sort() -> nums is now [-1, -1, 0, 1, 2]
#        prev = None
#        for index, num in enumurate(nums):
#            a = -1         
#        ref_b = 0 + 1 = 1
#        ref_c =  5 - 1 = 4
#        ref_b != len - 2
#        if (a == prev): don't take branch
#        while (ref_b < ref_c): 1 < 5 so looping
#            b = nums[1] = -1 
#            c = nums[4] = 2
#           compare_sum = -1 + -1 + 2 = 0
#            if 0 == 0:
#               output.append([-1, -1, -2])
#                ref_b += 1, ref_b is now 2
#            go to while loop again, 2 < 4
#            b = nums[2] = 0
#            c = nums[4] = 2
#            compare_sum = -1 + 0 + 2 = 1
#            compare_sum != 0, check elif
#            compare_sum is not < 0, go to else
#            ref_c -= 1, ref c = 3
#            while loop again because 2 < 3
#            b = nums[2] = 0
#            c = nums[3] = 1
#            compare_sum = -1 + 0 + 1 = 0
#            compare_sum == 0:
#            output.append([-1, 0, 1])
#            b += 1, b is now 3
#            loop invariant for while fails because 3 is not < 3
#            a = prev = -1
#            top of for loop
#            ref_b = 2
#            ref_c = 4
#            2 != 5 - 2
#            a == prev, 1 == -1
#            continue to next iteration of for loop
#            skip over 0 and ff to next interesting case
#            top of for loop
#            a = 1
#             