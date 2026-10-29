from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_check = defaultdict(int)
        if len(s) != len(t):
            return False
        for index in range(len(s)):
            anagram_check[s[index]] += 1
            anagram_check[t[index]] -= 1
        for key, value in anagram_check.items():
            if value != 0:
                return False
        return True

# Trace 1:
# Input: s = "jar", t = "jam"
#
# anagram_check is empty dict
# len(s) == len(t), so don't take branch

# for index in range(len(s)), len is 3 so we will loop over [0, 1, 2]
# anagram_check['j'] += 1
# anagram_check['j'] -= 1
# anagram_check = {'j': 0} - becasue + 1 - 1 = 0

# iteration 2:
# anagram_check['a'] += 1
# anagram_check['a'] -= 1
# anagram_check = {'j': 0, 'a': 0}

# iteration 3:
# anagram_check['r'] += 1
# anagram_check['m'] -= 1
# anagram_check = {'j': 0, 'a': 0, 'r': 1, 'm': -1}

# for key, value in anagram_check.items:
# so we are iterating over keys: 'j', 'a', 'r', 'm'
# so we are iterating over values: 0, 0, 1, -1
#   if value != 0:
#   return False
# return True

# iterating over the code above:
# loop 1: value = 0
# 0 == 0, so we don't take the branch
# loop 2: value = 0
# 0 == 0, so we don't take the branch
# loop 3: 1
# 1 != 0, so we take the branch
# return False