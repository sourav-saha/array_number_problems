## Leetcode: https://leetcode.com/problems/custom-sort-string/
## this is map problem

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #create a hasmap out of the s
        dict = {}
        for c in s:
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
                
        #traverse the order and make the new string from s
        res = []
        for c in order:
            if c in dict:
                res.append(c*dict[c])
                del dict[c]
                
        for k, v in dict.items():
            res.append(k*v)
        
        return "".join(res) 
      
      
# for explanation if not posible from code, check youtube video using hashmap solution.
