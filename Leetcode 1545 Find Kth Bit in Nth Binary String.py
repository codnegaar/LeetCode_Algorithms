'''
Leetcode 1545 Find Kth Bit in Nth Binary String

Given two positive integers n and k, the binary string Sn is formed as follows:
        S1 = "0"
        Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1
        
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:
        S1 = "0"
        S2 = "011"
        S3 = "0111001"
        S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

Example 1:
        Input: n = 3, k = 1
        Output: "0"
        Explanation: S3 is "0111001".
        The 1st bit is "0".

Example 2:
        Input: n = 4, k = 11
        Output: "1"
        Explanation: S4 is "011100110110001".
        The 11th bit is "1".
 
Constraints:
        1 <= n <= 20
        1 <= k <= 2n - 1
'''
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case: When n = 1, the binary string is "0"
        if n == 1:
            return '0'
        
        # Calculate the length of the current string S_n, which is 2^n - 1
        length_of_sn = (1 << n) - 1  # equivalent to 2^n - 1
        
        # Find the middle position of S_n
        middle_position = (length_of_sn // 2) + 1
        
        # If k is at the middle position, the bit is '1'
        if k == middle_position:
            return '1'
        
        # If k is in the first half, recursively find the bit in S_(n-1)
        if k < middle_position:
            return self.findKthBit(n - 1, k)
        
        # If k is in the second half, find the corresponding bit in S_(n-1) and invert it
        mirrored_k = length_of_sn - k + 1
        bit_in_sn_minus_1 = self.findKthBit(n - 1, mirrored_k)
        
        # Invert the bit ('0' becomes '1', '1' becomes '0')
        return '1' if bit_in_sn_minus_1 == '0' else '0'
