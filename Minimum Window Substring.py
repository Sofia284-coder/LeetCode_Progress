class Solution:
    def minWindow(self, s: str, t: str) -> str:

        required = {}
        t_map = {}

        minimum = math.inf #forgot that min need to be inf not 0

        min_string = ""

        for i in range(len(t)):

            if t[i] in required:

                required[t[i]] = required[t[i]] + 1
                t_map[t[i]] = t_map[t[i]] + 1
            
            else:
                required[t[i]] = 1
                t_map[t[i]] = 1

        print(required)
        print(t_map)

        window = {}

        l = 0
        r = 0

        while r < len(s):

            if s[r] in window:

                window[s[r]] = window[s[r]] + 1
            
            else:
                window[s[r]] = 1

            if s[r] in required:
                required[s[r]] = required[s[r]] - 1

                if required[s[r]] == 0:
                    required.pop(s[r])

            #window valid
            while required == {}:

                size = r - l + 1

                if size < minimum:

                    minimum = size
                    min_string = s[l:r+1]


                window[s[l]] = window[s[l]] - 1

                if s[l] in t_map: #use map for searching rather than seraching string, also forget to check this

                    if window[s[l]] < t_map[s[l]]:

                        required[s[l]] = 1

                l = l + 1

            r = r + 1

        return min_string

# we need to know what t requires → use a required frequency map.
# we need to know what the current window contains → use a window frequency map.
# expand r → add s[r] to the window and update its frequency.
# check validity → the window is valid when it contains at least the required frequency of every character in t (required becomes empty in our approach).
# once valid, record the window size → r - l + 1.
# move l to shrink the window → remove s[l] from the window map.
# check whether removing it affected validity → if the window now has fewer occurrences than required, add that requirement back.
# if still valid, keep moving l → continue looking for a smaller valid window.
# once invalid, stop shrinking and move r again.
# keep track of the smallest valid window found.
