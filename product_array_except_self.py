## Leetcde: https://leetcode.com/problems/product-of-array-except-self/
## classic problem of array pre-processing where we preprocess two arrays, 
## one contains the product of all the left elements of the current index i (pa)
## another contains the product of all the right elements of the current index i (sa)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pa = []
        sa = []
        
        #fill the pa array
        pa.append(1)
        i = 0
        for j in range(len(nums)):
        	# discard the last elem of the array for calculation
        	if j == len(nums) - 1:
        		break
        		
        	pa.append(nums[j] * pa[i])
        	i += 1
            
        #fill sa array
        sa.append(1)
        i = 0
        for j in reversed(range(len(nums))):
        	#discard the first elem of the array for reversed clculation 
        	if j == 0:
        		break
        	
        	sa.append(nums[j] * sa[i])
        	i += 1
            
        sa = list(reversed(sa))
        
        res = []
        for i in range(len(nums)):
            res.append(pa[i] * sa[i])
        return res
      
