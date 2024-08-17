'''
Leetcode 1937 Maximum Number of Points with Cost

You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.
To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.
However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1
(where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.
Return the maximum number of points you can achieve.

abs(x) is defined as:
                x for x >= 0.
                -x for x < 0. 

Example 1:
        Input: points = [[1,2,3],[1,5,1],[3,1,1]]
        Output: 9
        Explanation:
        The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
        You add 3 + 5 + 3 = 11 to your score.
        However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
        Your final score is 11 - 2 = 9.

Example 2:
        Input: points = [[1,5],[2,3],[4,2]]
        Output: 11
        Explanation:
        The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
        You add 5 + 3 + 4 = 12 to your score.
        However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
        Your final score is 12 - 1 = 11.
 
Constraints:
        m == points.length
        n == points[r].length
        1 <= m, n <= 105
        1 <= m * n <= 105
        0 <= points[r][c] <= 105

'''

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        
        for i in range(1, rows):
            # Initialize the right and left max arrays
            right_max = [0] * cols
            left_max = [0] * cols
            
            # Fill the right_max array, moving from right to left
            right_max[-1] = points[i-1][-1]
            for j in range(cols - 2, -1, -1):
                right_max[j] = max(right_max[j+1] - 1, points[i-1][j])
            
            # Fill the left_max array, moving from left to right
            left_max[0] = points[i-1][0]
            for j in range(1, cols):
                left_max[j] = max(left_max[j-1] - 1, points[i-1][j])
            
            # Update the current row in points with the maximum possible points
            for j in range(cols):
                points[i][j] += max(left_max[j], right_max[j])
        
        # The maximum points will be in the last row of points
        return max(points[-1])
