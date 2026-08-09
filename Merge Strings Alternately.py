class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merged = ""

        #we first check which string has lesser length

        length = min(len(word1), len(word2))

        #then we loop both till that length

        for i in range(length):
            merged += word1[i]
            merged += word2[i]

        #if any ones length is still greater than the loop, we append the remaining ones

        if len(word1) > length:
            merged += word1[length:len(word1)]

        elif len(word2) > length:
            merged += word2[length:len(word2)]

        return merged


        
