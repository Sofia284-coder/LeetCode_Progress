class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l = 0
        r = k

        max = 0

        while (r <= len(nums)):

            sum = 0

            for i in range(l, r):

                print(nums[i])

                sum = sum + nums[i]

            avg = sum/k

            if avg > max:
                max = avg
            
            l = l + 1

            r = r + 1

        return max


#so we well keep track of window with two variables and move them forward and calculate average for that window through loop
#okay but how to know when to end?
#if the right index becomes greater than the k then end?
#no not greater than k, greater than length
#first try on paper and dry run then start implementing
#also check for edge cases, sometimes tey point towards a cleaner approach

#Mistakes i was making: onlly calculated sum forgot to take average
#forgot how range works, range(0,4) means 0,1,2,3
