class Solution:
    def reverseString(self, s: list[str]) -> None:
        
        l = 0
        r = len(s) - 1

        while l <= r:

            s[l],s[r] = s[r],s[l]

            l+=1
            r-=1

#Learned what two-pointer approach is, and what in-place shifting means
