# 8. Longest Increasing Subsequence
# 300. Longest Increasing Subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        # results list stores how many smaller numbers before the number at the index
        results = [0 for _ in range(n)]
        for i in range(n):
            length, maxLis = 1, 0
            # nums[j] iterate through all the nums before nums[i]
            for j in range(i - 1, -1, -1):  # range(start, stop, step)
                # if there is a smaller number before current number,
                # add the number of smaller number of the smaller number found (nums[j])
                # to the number of smaller number of the current number (nums[i])
                if nums[j] < nums[i]:
                    maxLis = max(maxLis, results[j])
            # if there are no smaller number before it, the result would be 1
            # if there are some smaller numbers before it, the max value of
            # the number of smaller number of the smaller number found (nums[j]) is taken
            results[i] = maxLis + 1

        return max(results)
