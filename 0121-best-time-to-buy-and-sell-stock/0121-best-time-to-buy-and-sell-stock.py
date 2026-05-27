class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_pri = prices[0]
        for price in prices:
            if price < min_pri:
                min_pri = price
            cur_pro = price - min_pri
            profit = max(cur_pro , profit)
        return profit



        # for i in range(len(prices) - 1):
        #     right = i + 1
        #     max_p = 0
        #     while right < (len(prices )- 2):
        #         if  prices[i + 1] > prices[i]:
        #             max_p = max(max_p , prices[i + 1])
        #         right += 1
        #     profit += max_p
        # return profit