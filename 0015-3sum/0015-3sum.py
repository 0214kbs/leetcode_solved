class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            left = i+1
            right = len(nums)-1
            while left<right:
                sumv = nums[i]+nums[left]+nums[right]
                if sumv == 0:
                    answer.append([nums[i], nums[left],nums[right]])
                    while left<right and nums[left] == nums[left+1]: left +=1
                    while left<right and nums[right] == nums[right-1]: right -=1
                    left +=1
                    right -=1
                elif sumv > 0:
                    right -= 1
                else:
                    left +=1
        
        return answer