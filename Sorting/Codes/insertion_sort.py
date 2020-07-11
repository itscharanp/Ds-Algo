"""
Insertion Sort
The task is to complete insert() function which is used to implement Insertion Sort.

Input:
First line of the input denotes number of test cases T. First line of the testcase is the size of array N and second line consists of array elements separated by space.

Output:
Sorted array in increasing order is displayed to the user.

User Task:
Since this is a functional problem you don't a have to worry about input, you just have to complete the function insert(). The printing is done automatically by the driver code.

Constraints:
1 <= T <= 50
1 <= N <= 1000
1 <= arr[i] <= 1000

Example:
Input:
2
5
4 1 3 9 7
10
10 9 8 7 6 5 4 3 2 1
Output:
1 3 4 7 9
1 2 3 4 5 6 7 8 9 10

Explanation:
Testcase 1: The array after perfoming insertion sort: 1 3 4 7 9.
Testcase 2: The array after performing insertion sort: 1 2 3 4 5 6 7 8 9 10.

 

** For More Input/Output Examples Use 'Expected Output' option **
"""

def insert(arr):
    n=len(arr)
    for x in range(len(arr)):
        p = arr.index(max(arr[:n-x]))
        temp = arr[n-x-1]
        arr[n-x-1] = arr[p]
        arr[p] = temp
