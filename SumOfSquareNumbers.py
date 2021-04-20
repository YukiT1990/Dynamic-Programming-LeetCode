# 9. Sum of Square numbers
# 633. Sum of Square Numbers

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        n = int(math.sqrt(c))

        squareList = [0 for _ in range(n + 1)]

        for i in range(n + 1):
            squareList[i] = i**2
        left = 0
        right = n

        while (left <= right):
            # found
            if (squareList[left] + squareList[right]) == c:
                return True
            # the sum is bigger than c
            elif (squareList[left] + squareList[right]) > c:
                right -= 1
            # the sum is smaller than c
            else:
                left += 1
        # not found
        return False
        
