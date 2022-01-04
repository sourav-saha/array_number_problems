# leetcode:
# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []
        
        #fill the left array
        for i in range(len(height)):
            if i == 0:
                left.append(height[i])
            else:
                left.append(max(left[i-1], height[i]))
                
        #fill the right array
        j = 0
        for i in reversed(range(len(height))):
            if i == (len(height)-1):
                #right.append(height[i])
                right.insert(0, height[i])
            else:
                right.append(max(right[j-1], height[i]))
            j += 1
        
        right = list(reversed(right))
        
        
        s = 0
        for i in range(len(height)):
            s += min(left[i], right[i]) - height[i]
        
        return s
        
        
