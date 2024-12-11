class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k>len(nums):
            k = k%len(nums)
        tmp = [n for n in nums]
        for i in range(len(nums)):
            if i<k:
                nums[i] = tmp[len(nums)-k+i]
            else:
                nums[i] = tmp[i-k]