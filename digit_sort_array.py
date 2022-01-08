## Hackerrank : https://www.hackerrank.com/contests/bz-cci-53/challenges/bz-digit-sum-sort/problem
'''
Given an array A of size N. You need to sort the contents of this array in ASCENDING ORDER of digit sum of elements. If two numbers have same digit sum, then bigger number should be placed first, smaller should be second.

Input Format

The first line contains a single integers N denoting the size of the array. The next line contains N space separated integers denoting the contents of the array.

Constraints

1 <= N <= 105
1 <= Ai <= 109

Output Format

Print N space separated integers, i.e. the final sorted array.

Sample Input 0

7
20 88 975 1 0 40 22
Sample Output 0

0 1 20 40 22 88 975
'''

from functools import cmp_to_key

def digitsum(n)->int:
    s = 0
    while n!= 0:
        s += n%10
        n //= 10
    return s

def compare(a, b):
    da = digitsum(a)
    db = digitsum(b)
    
    if da > db:
        return 1
    elif da < db:
        return -1
    else:
        if a < b:
            return 1
        else:
            return -1

def my_sort(arr, n)->list[int]:
    res = sorted(arr, key=cmp_to_key(compare))
    return res
        

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(*my_sort(arr, n))
    
