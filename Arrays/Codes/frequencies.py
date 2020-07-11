"""
Frequencies of Limited Range Array Elements
Given an array A[] of N positive integers which can contain integers from 1 to N where elements can be repeated or can be absent from the array. Your task is to count frequency of all elements from 1 to N.

Note: Expected time complexity is O(n) with O(1) extra space.

Input Format:
First line of input contains an integer T denoting the number of test cases. For each test case, first line contains an integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output Format:
For each test case, output N space-separated integers denoting the frequency of each element from 1 to N.

Your Task:
You need to complete the function printfrequency and print frequency of each element. The newline is automatically added by the driver code.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 107
1 <= A[i] <= 106

Example:
Input:
2
5
2 3 2 3 5
4
3 3 3 3

Output:
0 2 2 0 1
0 0 4 0

Explanation:
Testcase 1: Counting frequencies of each array elements, we have:
1 occurring 0 times.
2 occurring 2 times.
3 occurring 2 times.
4 occurring 0 times.
5 occurring 1 time.
Testcase 2: Counting frequencies of each array elements, we have:
1 occurring 0 times.
2 occurring 0 times.
3 occurring 4 times.
4 occurring 0 times.

** For More Input/Output Examples Use 'Expected Output' option **
"""

def printfrequency(A,N):
    s = [0]*N
    for x in A:
        s[x-1] += 1
    for l in s:
        print(l,end=" ")