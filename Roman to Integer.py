# If the current Roman numeral is smaller than the numeral I just saw on its right, subtract it. Otherwise add it.


class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        last = 0

        for i in range(len(s) - 1, -1, -1):

            curr = map[s[i]]

            if curr < last:
                total -= curr
            else:
                total += curr

            last = curr

        return total
