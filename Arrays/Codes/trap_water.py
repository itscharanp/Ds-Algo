"""
Trapping Rain Water
Given an array arr[] of N non-negative integers representing height of blocks at index i as Ai where the width of each block is 1. Compute how much water can be trapped in between blocks after raining.
Structure is like below:
|  |
|_|
We can trap 2 units of water in the middle gap.



Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. Each test case contains an integer N denoting the size of the array, followed by N space separated numbers to be stored in array.

Output:
Output the total unit of water trapped in between the blocks.

User Task:
The task is to complete the function trappingWater() which returns the total amount of water that can be trapped.

Constraints:
1 <= T <= 100
3 <= N <= 107
0 <= Ai <= 108

Example:
Input:
2
4
7 4 0 9
3
6 9 9

Output:
10
0

Explanation:
Testcase 1: Water trapped by block of height 4 is 3 units, block of height 0 is 7 units. So, total unit of water trapped is 10 units.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""
import math
def trappingWater(arr,n):
    p=[]
    s=[]
    reva = arr[::-1]
    mi = -math.inf
    ma = -math.inf
    for x in range(n):
        ma = max(ma,arr[x])
        p.append(ma)
        mi = max(mi,reva[x])
        s.append(mi)
    s= s[::-1]
    ans = 0
    for x in range(n):
        if(min(s[x],p[x]) - arr[x] >0):
            ans+= min(s[x],p[x]) - arr[x]
    return(ans)
