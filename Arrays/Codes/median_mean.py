"""
Mean And Median of Array
Given an array a[ ] of size N. The task is to find the median and mean of the array elements. Mean is average of the numbers and median is the element which is smaller than half of the elements and greater than remaining half.  If there are odd elements, median is simply the middle element. If there are even elements, then median is floor of average of two middle numbers. If mean is floating point number, then we need to print floor of it.

Note: To find the median, you might need to sort the array. Since sorting is convered in later tracks, we have already provided the sort function to you in the code.

Input Format: 
The first line of input contains a single integer T denoting the number of test cases. Then T test cases follow. Each test case consist of two line input, 1st line is the size of array and the 2nd line is the integer array elements.

Output Format: 
For each testcase, in a new line, print the space separated mean and median of the array elements.

Your Task:
This is a function problem. You just need to complete the following two function:

mean(): It takes the array and its size N as parameters and returns the mean as an integer.
median(): It takes the array and its size N as parameters and returns the median as an integer.
Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= a[i] <= 106

Example:
Input:
2
5
1 2 19 28 5
4
2 8 3 4

Output:
11 5
4 3

Explanation:
Testcase 1: For array of 5 elements, mean is (1 + 2 + 19  + 28  + 5)/5 = 11.  Median is 5 (middle element after sorting)
Testcase 2: For array of 4 elements, mean is floor((2 + 8 + 3 + 4)/4) = 4.  Median is floor((4 + 3)/2) = 3

** For More Input/Output Examples Use 'Expected Output' option **
"""
import math
def median(A,N):
    
    A.sort()
    if(len(A)%2==0):
        return( math.floor((A[N//2 - 1] + A[N//2])/2) )
    else:
        return( math.floor(A[N//2]) )
    
    
def mean(A,N):
    return(math.floor(sum(A)/N))

assert mean([1,2,19,28,5],5) == 11
assert median([1,2,19,28,5],5) == 5

print('The code ran Correctly')
