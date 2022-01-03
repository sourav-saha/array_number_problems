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

def find_largest_no(a, n):
    res = ""
    b = sorted(a, key=cmp_to_key(compare))
    #print(b)
    for item in b:
        res += str(item)
    return res

if __name__ == "__main__":
    T = int(input().strip())
    for ti in range(T):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        #find_largest_no(a, n)
        print(find_largest_no(a, n))
