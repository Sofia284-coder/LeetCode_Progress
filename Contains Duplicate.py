class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


# My first thought was using python dictionary but since we only have to see  if it appeared before and not how many time it appeared, so set was used.
