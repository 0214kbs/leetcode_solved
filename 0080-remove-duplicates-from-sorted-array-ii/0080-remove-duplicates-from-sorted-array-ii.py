class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        cur =2
        for ni in range(2,len(nums)):
            if nums[ni] == nums[cur-1] == nums[cur-2]:
                continue
            nums[cur] = nums[ni]
            cur += 1
        for _ in range(len(nums)-cur):
            nums.pop()
        return len(nums)