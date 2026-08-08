class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        
        result = [intervals[0]]

        length = len(intervals)

        if  length == 1:
            return intervals

        for i in range(1, len(intervals)):

            if result[-1][1] >= intervals[i][0]:
                result[-1] = [result[-1][0], max(intervals[i][1], result[-1][1])]
            else:
                result.append(intervals[i])

        
        return result


# At first I misunderstood the question and thought we only have to find overlapping in between 2 intervals (which incorrectly lead me to use curr and next pointers)
# and i forgot to consider the edge case of only one interval

# Lesson: Understand first and then code
