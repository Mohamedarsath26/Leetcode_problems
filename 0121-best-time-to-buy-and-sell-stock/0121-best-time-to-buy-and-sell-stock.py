class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        min_price = float('inf')  # Track the minimum price encountered so far
        
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]  # Update the minimum price if the current price is lower
            else:
                # Calculate profit if sold on the current day
                prof = prices[i] - min_price
                max_prof = max(max_prof, prof)  # Update the maximum profit
                
        return max_prof
