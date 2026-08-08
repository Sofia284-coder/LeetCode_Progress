class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        maxSum = nums[0]
        current_sum = nums[0]

        for i in range(1,len(nums)):

            current_sum = max(nums[i], current_sum + nums[i])

            maxSum = max(maxSum,current_sum)

        return maxSum

# At each point we keep adding the previous values then if at any point the sum including the previosu values is 
# less the current value then we just choose the current value as the sum and check if it's biggers than the previous maximum sum
