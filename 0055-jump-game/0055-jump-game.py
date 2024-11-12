class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        maxv = 0
        for ni, num in enumerate(nums):
            if ni > maxv: return False
            maxv = max(ni+num, maxv)
            if maxv > len(nums): return True
        return False