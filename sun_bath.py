'''
This prob is similar to rain water ytrap problem

There are N buildings in a row each having a height  A person standing on a building can see the sun only if there are no obstructions between the sun and him. A person can see the sun either in the Morning or in the Evening. Output the no. of people who can see the sun in a day.

West indicates left of the row
East indicates right of the row
Note:A building of height  is not an obstruction for another building of height  if 
Input Format

First line contains the no. of test cases T.
First line of each test case consists of N.
Next line contains N spaced integers denoting the heights of the buildings.

Constraints


Output Format

For each test case, print the no. of people who can watch the Sun in a day.

Sample Input 0

2
5
1 2 1 2 1
5
3 2 1 2 3
Sample Output 0

4
2
Explanation 0

For the first test case,
Person 1 can see the sun in the Evening.
Person 2 can see the sun in the Morning and Evening.
Person 3 cannot see the sun.
Person 4 can see the sun in the Morning and Evening.
Person 5 can see the sun in the Morning.
'''


def find_person(arr, n):
    left = [] #left = [0]*n
    for i in range(n):
        if i == 0:
            left.append(arr[i])
        else:
            left.append(max(left[i-1], arr[i]))
    
    right = []
    for i in reversed(range(n)):
        if i == n-1:
            right.insert(0, arr[i])
        else:
            right.insert(0, max(right[0], arr[i]))
            
    count = 0
    for i in range(n):
        if min(left[i], right[i])-arr[i] == 0:
            count += 1
            
    return count
        

if __name__ == "__main__":
    T = int(input().strip())
    for ti in range(T):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        print(find_person(arr, n))
        
