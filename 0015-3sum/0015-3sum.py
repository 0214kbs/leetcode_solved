class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = set()
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[i]+nums[left]+nums[right] == 0:
                    answer.add((nums[i], nums[left],nums[right]))
                    left +=1
                elif nums[i]+nums[left]+nums[right] > 0:
                    right -= 1
                else:
                    left +=1
        
        return list(answer)