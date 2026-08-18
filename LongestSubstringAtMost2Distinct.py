class Solution:
    def longestSubstring(self, s: str) -> int:

        #we have to have l and r
        # we keep moving right but when we encounter a wrong window,
        # we shift l until the window is correct
        # Challanges: how do we check and how do we keep track of valid window sizes?
        #Checking: when we encounter third distinct value, window is invalid, 
        # so the window before that is
        # we keep track of how big the windows is through the through l and r
        # what about the current value that invalidated the window and moving forward?

        #Critical Gap: we keep checking the size of current valid window after every time we expand it, 
        # the window being in valid is not the trigger to count

        map = {}

        max = 0
        r = 0
        l = 0


        while r <= len(s)-1:
    
            # print(s[r])

            if s[r] in map:

                map[s[r]] = map.get(s[r]) + 1

            else:
                map[s[r]] = 1

            # print(map)


            while (len(map) >= 3):

                map[s[l]] = map.get(s[l]) - 1
                
                if map[s[l]] == 0:

                    map.pop(s[l])

                # print("Length",len(map))

                l = l + 1

            size = r - l + 1

            # print("Size: ",size)

            if size > max:

                max = size


            r = r + 1

    

        return max

                 
if __name__ == "__main__":

    s = Solution()
    print(s.longestSubstring("ccaabbb"))
    print(s.longestSubstring("eceba"))
    print(s.longestSubstring("geekforgeeks"))
    print(s.longestSubstring("c"))
    print(s.longestSubstring("ca"))
