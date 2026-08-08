class Solution:
    
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        hashmap = {}

        list_one = []
        list_two = []

        for num in nums1:

            hashmap[num] = 1

        # print (hashmap)

        for num in nums2:

            if num in hashmap:

                old = hashmap[num]

                hashmap[num] = old + 1
            else:
                hashmap[num] = -1000
                list_two.append(num)
            # print(list_two)

        for key, value in hashmap.items():
            if value == 1:
                list_one.append(key)
            # print(list_one)
        
        return [list_one, list_two]



# Although this approach solves this, i later learned that it wasn't optimal as there was no need to keep track of count, we only needed to know what existed
# so using python set would have been best as it O(1)
