class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum = 0
        maxSum = nums[0]
        for i in nums:
            curSum = max(curSum, 0)
            curSum += i
            maxSum = max(maxSum, curSum)
        return maxSum