## Leetcode: 
## https://leetcode.com/problems/4sum-ii/


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dict = {}
        count = 0
        for n1 in nums1:
            for n2 in nums2:
                s = n1 + n2
                if s in dict:
                    dict[s] += 1
                else:
                    dict[s] = 1
                    
        for n3 in nums3:
            for n4 in nums4:
                s1 = n3 + n4
                if (0 - s1) in dict:
                    count += dict[0-s1]
                    
        return count
