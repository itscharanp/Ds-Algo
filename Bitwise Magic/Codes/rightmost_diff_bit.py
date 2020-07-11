"""
Rightmost different bit
Given two numbers M and N. The task is to find the position of rightmost different bit in binary representation of numbers.

Input Format:
The input line contains T, denoting the number of testcases. Each testcase follows. First line of each testcase contains two space separated integers M and N.

Output Format:
For each testcase in new line, print the position of rightmost different bit in binary representation of numbers. If both M and N are same then print -1 in this case.

User Task:
The task is to complete the function posOfRightMostDiffBit() which takes two arguments m and n and returns the position of first different bits in m and n.

Constraints:
1 <= T <= 100
1 <= M <= 103
1 <= N <= 103

Example:
Input:
2
11 9
52 4

Output:
2
5

Explanation:
Tescase 1: Binary representaion of the given numbers are: 1011 and 1001, 2nd bit from right is different.
Testcase 2: Binary representation of the given numbers are:  ‭110100‬ and 0100, 5th bit fron right is different.

** For More Input/Output Examples Use 'Expected Output' option **
"""
import math
def posOfRightMostDiffBit(m,n):
    ans = m^n
    return(int(math.log((ans & -ans),2)+1))
    
assert posOfRightMostDiffBit(11,9) == 2
assert posOfRightMostDiffBit(52,4) == 5
assert posOfRightMostDiffBit(8,0) == 4

print('The code ran Correctly')

