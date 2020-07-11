"""
Find first set bit
Given an integer an N. The task is to print the position of first set bit found from right side in the binary representation of the number.

Input:
The first line of the input contains an integer T, denoting the number of test cases. Then T test cases follow. The only line of the each test case contains an integer N.

Output:
For each test case print in a single line an integer denoting the position of the first set bit found form right side of the binary representation of the number. If there is no set bit print "0".

User Task:
The task is to complete the function getFirstSetBit() that takes n as parameter and returns the the position of first set bit.

Constraints:
1 <= T <= 200
0 <= N <= 106

Example:
Input:
3
18
12
0

Output:
2
3
0

Explanation:
Testcase 1: Binary representation of 18 is 010010, the first set bit from the right side is at position 2.
Testcase 2: Binary representation of  12 is 1100, the first set bit from the right side is at position 3.
Testcase 3: In 0 there is no set bit so we print 0 as mentioned.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""

import math
def getFirstSetBit(n):
    if(n==0):
        return(0)
    return(int(math.log(n & -n , 2))+1)

assert getFirstSetBit(18) == 2
assert getFirstSetBit(4) == 3
assert getFirstSetBit(0) == 0

print('The code ran Correctly')