class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left, right = 0, 1
        maxP = 0
        
        while right < len(prices):
            if prices[left] <= prices[right]:
                maxP = max(maxP, prices[right] - prices[left])
            else:
                left = right
            right += 1
        
        return maxP