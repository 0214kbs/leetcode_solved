class Solution(object):
    def majorityElement(self, nums):
        dic = {}
        for n in nums:
            if n in dic: 
                dic[n] +=1
                if dic[n] > len(nums)//2: 
                    return n
            else: dic[n] = 1