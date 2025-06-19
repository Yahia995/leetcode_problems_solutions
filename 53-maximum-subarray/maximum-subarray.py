class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = 0
        maxSum = nums[0]
        for i in nums:
            curSum += i
            maxSum = max(maxSum, curSum)
            curSum = max(curSum, 0)
        return maxSum