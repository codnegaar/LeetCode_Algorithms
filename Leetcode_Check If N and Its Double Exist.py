'''
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 

Constraints:

2 <= arr.length <= 500
-103 <= arr[i] <= 103
   Hide Hint #1  
Loop from i = 0 to arr.length, maintaining in a hashTable the array elements from [0, i - 1].
   Hide Hint #2  
On each step of the loop check if we have seen the element 2 * arr[i] so far or arr[i] / 2 was seen if arr[i] % 2 == 0.

'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        lookup = set()
        for x in arr:
            if 2*x in lookup or (x%2 == 0 and x//2 in lookup):
                return True
            lookup.add(x)
        return False
        
