'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:
        Input: points = [[1,1],[2,2],[3,3]]
        Output: 3
        
Example 2:
        Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        Output: 4
        
 Constraints:
        1 <= points.length <= 300
        points[i].length == 2
        -104 <= xi, yi <= 104

'''

class Solution:
  def maxPoints(self, points: List[List[int]]) -> int:
    ans = 0

    def gcd(a: int, b: int) -> int:
      return a if b == 0 else gcd(b, a % b)

    def getSlope(p: List[int], q: List[int]) -> Tuple[int, int]:
      dx = p[0] - q[0]
      dy = p[1] - q[1]
      if dx == 0:
        return (0, p[0])
      if dy == 0:
        return (p[1], 0)
      d = gcd(dx, dy)
      return (dx // d, dy // d)

    for i, p in enumerate(points):
      slopeCount = collections.defaultdict(int)
      samePoints = 1
      maxPoints = 0
      for j in range(i + 1, len(points)):
        q = points[j]
        if p == q:
          samePoints += 1
        else:
          slope = getSlope(p, q)
          slopeCount[slope] += 1
          maxPoints = max(maxPoints, slopeCount[slope])
      ans = max(ans, samePoints + maxPoints)

    return ans
