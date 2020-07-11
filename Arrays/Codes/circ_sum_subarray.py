"""
Max Circular Subarray Sum
Given an array arr[] of N integers arranged in a circular fashion. Your task is to find the maximum contigious subarray sum.

Input:
First line of input contains a single integer T which denotes the number of test cases. First line of each test case contains a single integer N which denotes the total number of elements. Second line of each test case contains N space separated integers denoting the elements of the array.

Output:
For each test case print the maximum sum obtained by adding the consecutive elements.

User Task:
The task is to complete the function circularSubarraySum() which finds the circular subarray with maximum sum.

Constraints:
1 <= T <= 101
1 <= N <= 106
-106 <= Arr[i] <= 106

Example:
Input:
3
7
8 -8 9 -9 10 -11 12
8
10 -3 -4 7 6 5 -4 -1
8
-1 40 -14 7 6 5 -4 -1

Output:
22
23
52

Explanation:
Testcase 1: Starting from last element of the array, i.e, 12, and moving in circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.
 

** For More Input/Output Examples Use 'Expected Output' option **
"""
def circularSubarraySum(arr,n):
    neg_vals, max_num = True, max(arr)
    ans = maxSubArraySum(n, arr)
    i = curr = 0
    for i in range(n):
        if arr[i] > 0:
            neg_vals = False
        curr += arr[i]
        arr[i] = -arr[i]
    if neg_vals:
        return max_num
    curr = curr + maxSubArraySum(n, arr)
    return max(ans, curr)
    
def maxSubArraySum(a,size):
    max1 = 0
    max2 = 0
    for i in range(size):
        max2 = max2 + a[i]
        if(max2 < 0):
            max2 = 0
        if(max1 < max2):
            max1 = max2
    if(max1<=0):
        return(max(a))
    return max1