# Problem 3: Best Time to Buy & Sell Stock

# LeetCode ID: 121

# Pattern: Prefix Min / Max / Running difference

# Goal: Practice tracking min/max while iterating

# Steps:

# Initialize minPrice = arr[0], maxProfit = 0.

# Traverse array from index 1:

# Update minPrice = min(minPrice, arr[i])

# Update maxProfit = max(maxProfit, arr[i] - minPrice)

# Return maxProfit.

# Focus: Understand why you don’t need nested loops — the prefix tracking handles it in one pass

#Key mindset shift: we treat each day as a sell dy and look for the best buy time before it


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        mininum = prices[0]
        maxProfit = 0

        for i in range(1,len(prices)):

            mininum = min(prices[i], mininum)

            maxProfit = max(maxProfit,prices[i] - mininum)

        return maxProfit
      
# after 3 failed attempts and failing to grasp the logic, i did end up looking over to chatGPT for the solution but the struggle heled me find gaps in my thinking.

                 
