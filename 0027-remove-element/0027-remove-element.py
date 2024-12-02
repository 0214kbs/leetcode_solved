class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        res_i = 0
        for check_i in range(0, len(nums)):
            if nums[check_i] != val:
                nums[res_i] = nums[check_i]
                res_i += 1
        return res_i