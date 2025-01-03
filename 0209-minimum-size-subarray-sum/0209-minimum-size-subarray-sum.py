from collections import deque
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] >= target: return 1
        MAXV = 10**5+1
        answer = MAXV
        left, right = 0,0
        cur = nums[0]
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