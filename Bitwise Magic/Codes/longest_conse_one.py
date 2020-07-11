"""
Longest Consecutive 1's
Given a number N. The task is to find the length of the longest consecutive 1s in its binary representation.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer N.

Output:
For each test case, in a new line, print the length of the longest consecutive 1's in N's binary representation.

User Task:
The task is to complete the function maxConsecutiveOnes() which returns the length of longest consecutive 1s in the binary representation of given N.

Constraints:
1 <= T < 100
1 <= N <= 103

Example:
Input:
2
14
222

Output:
3 
4

Explanation:
Testcase 1: Binary representation of 14 is 1110, in which 111 is the longest consecutive set bits of length is 3.
Testcase 2: Binary representation of  222 is 11011110, in which 1111 is the longest consecutive set bits of length 4.

** For More Input/Output Examples Use 'Expected Output' option **
"""
def maxConsecutiveOnes(x):
    count = 0
    while x!=0:
        x = x & (x<<1)
        count+=1
    
    return count

assert maxConsecutiveOnes(14) == 3
assert maxConsecutiveOnes(222) == 4

print('The code ran Correctly')