class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        max_profit = 0
        
        for i in range(1,len(prices)):
            
            cur_price = prices[i]
            
            min_price = min(cur_price, min_price)
            profit = cur_price - min_price
            
            max_profit =  max(profit, max_profit)
        return max_profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    sol = Solution()
    print("max_profit: ",sol.maxProfit(prices))
