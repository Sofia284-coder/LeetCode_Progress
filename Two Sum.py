class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hashmap = {}

        for i in range(len(nums)):

            if (target - nums[i]) not in hashmap:

                hashmap[nums[i]] = i

            else:
                return [i, hashmap[target-nums[i]]]

# First did using nested loop the learned the hashmap approach, trying both approaches helped me understand when to use hashmap.

# i identified a rule: can you use the values we have seen again to find the solution instaed of iterating again
