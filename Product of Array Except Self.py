class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        #prefix product:

        pre_pro = [1]
        pre = 1
        
        for i in range(1, len(nums)):

            pre = pre * nums[i-1] 

            pre_pro.append(pre)

        print(pre_pro)

        pro_pro = [1]
        pro = 1

        for i in range(len(nums)-1,0,-1):

            pro = pro * nums[i]

            pro_pro.append(pro)

        print(pro_pro)

        res = []

        minus = len(pro_pro) - 1

        for i in range(len(pro_pro)):

            res.append(pre_pro[i] * pro_pro[minus - i])

        return res


if __name__ == "__main__":

    s = Solution()
    print(s.productExceptSelf([5,2,3,4])) 


# By far took me the longest time, as i kept dry running it to figure out how to multiply and have the result in the correct index
