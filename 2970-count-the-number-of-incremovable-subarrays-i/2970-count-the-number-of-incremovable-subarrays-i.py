class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        answer = 0

        for cnt in range(1, len(nums)+1):
            for i in range(0, len(nums)-cnt+1):
                subarr = nums[i:i+cnt]
                # print(subarr)
                start = 0   
                flag = True
                for j in range(len(nums)):
                    if j < i or j>=i+cnt:
                        if start < nums[j]:
                            start = nums[j]
                        else:
                            flag = False
                            break
                if flag:
                    answer +=1
        return answer