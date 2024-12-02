class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1 and nums[0] == val:
            nums = []
            return len(nums)
        
        last = len(nums) -1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] != val:
                last = i
                break
        
        for i in range(len(nums)):
            if last <= i: break
            if nums[i] == val:
                nums[i] = nums[last]
                
                last -=1
                while last>=i:
                    if nums[last] != val: break
                    if nums[last] == val: last -= 1
                
        nums = nums[:last+1]
        return len(nums)