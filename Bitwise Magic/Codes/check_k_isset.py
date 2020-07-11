"""
Check whether K-th bit is set or not
Given a number N and a bit number K, check if Kth bit of N is set or not. A bit is called set if it is 1. Position of set bit '1' should be indexed starting with 0 from LSB side in binary representation of the number.
Example, Consider N = 4(100):  0th bit = 0, 1st bit = 0, 2nd bit = 1.

Input Format:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case contain an integer  N. The second line of each test case contains an integer  K.

Output Format:
Corresponding to each test case, print "Yes" (without quotes) if Kth  bit is set else print "No" (without quotes) in a new line.

Your Task:
This is a function problem. You only need to complete the function checkKthbit that takes n and k as parameters and returns either true (if kth bit is set) or false(if kth bit is not set).

Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 109
0 ≤ K ≤ floor(log2(N) + 1)

Example:
Input:
3
4
0
4
2
500
3

Output:
No
Yes
No

Explanation:
Testcase 1: Binary representation of 4 is 100, in which 0th bit from LSB is not set. So, answer is No.
Testcase 2: Binary representation of 4 is 100, in which 2nd bit from LSB is set. So, answer is Yes.
Testcase 3: Binary representation of 500  is 111110100, in which 3rd bit from LSB is not set. So, answer is No.

 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def checkKthBit(n,k):
    q = (1<<k) & n
    return(q)

assert checkKthBit(4,0) == 0
assert checkKthBit(4,2) >= 1
assert checkKthBit(500,3) == 0

print('The code ran Correctly')