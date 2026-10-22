class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum() and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

# Trace 1: input "? abba !"

# left is 0
# right is 9 - 1 = 8
# we enter the while loop because left le right, 0 le 7
# we enter the nested while because s[0] = "?" which is not alphanumeric
# increment left to be equal to 1
# check again and see that s[left] is still not alphanumeric(a space)
# we increment left again and now left = 2
# left is alphanumeric so the loop condition is invalid, exit the while
# s[7] is not alphanumeric so we decrement, to 6, which s[7] is also non-alpha, so we decrement to 5
# s[5] is alphanumeric so we exit the inner while
# check if left ge right(2 ge 6 is not true), check if s[left] ne s[right](not true because a = a)
# increment left to 3, decrement right to 4
# go to top of the loop and see that 3 <= 4, so we continue in the loop
# s[3] = b so it is alphanumeric. loop condition not met so go to line 8
# s[4] = b so it is alphanumeric. loop condition not met so go to line  10
# 3 < 4 and s[3] = s[4] so if block not met on line 10
# increment(4) left(3) and increment right
# go to line 5 and left is not le than right so exit loop
# return True(is a palindrome)

# Trace 2: "aca"
# left = 0
# right = 3 - 1 = 2
# left is alphanum so don't enter left loop
# right is alphanum so don't enter right loop
# a = a so don't take conditional branch
# increment left to 1 and decrement right to 1
# at top of loop 1 <= 1 so continue iteration
# no non-alpha so don't take either adjustment loop
# left is ge right so we return false