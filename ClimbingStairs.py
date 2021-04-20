# 1. Climbing Stairs
# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        results = [0 for _ in range(46)]
        results[1] = 1
        results[2] = 2
        for i in range(3, n + 1):
            results[i] = results[i - 1] + results[i - 2]
        return results[n]
