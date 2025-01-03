from collections import deque
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == target: return 1
            else: return 0
        if nums[0] >= target: return 1
        MAXV = 10**5
        answer = MAXV   
        left = 0
        right = 0
        cur = nums[left]
        while right < len(nums):
            if cur < target:
                right +=1
                if right == len(nums): continue
                cur += nums[right]
            else:
                answer = min(answer, right-left+1)
                if left == right: 
                    left +=1 
                    right +=1
                    if right == len(nums): continue
                    cur = nums[right]
                else:
                    cur -= nums[left]
                    left += 1
        if answer == MAXV : return 0
        else: return answer