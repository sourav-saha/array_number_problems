## Leetcode problem link:
## https://leetcode.com/problems/largest-number/

from functools import cmp_to_key

def compare(s1, s2):
    str1 = str(s1) + str(s2)
    str2 = str(s2) + str(s1)
    if str1 > str2:
        return -1
    else:
        return 1
    

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #special case if the array has all 0s
        if nums.count(0) == len(nums):
            return "0"
        
        res = ""
        a = sorted(nums, key=cmp_to_key(compare))
        for item in a:
            res += str(item)

        return res
