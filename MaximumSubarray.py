# 13. Maximum Subarray
# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        maxLis[1] = max(maxLis[0] + nums[1], nums[1])
        maxLis[2] = max(maxLis[1] + nums[2], nums[2])
        """

        maxLis = [0 for _ in range(len(nums))]
        maxLis[0] = nums[0]

        for i in range(1,len(nums)):
            # take bigger one between the maximum sum until nums[i]
            # and current element itself (nums[i])
            maxLis[i] = max(maxLis[i-1] + nums[i], nums[i])
        return max(maxLis)
