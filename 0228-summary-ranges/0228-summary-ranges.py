class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        if len(nums) == 0: return []
        start = nums[0]
        end = nums[0]
        for ni in range(1,len(nums)):
            if nums[ni] == end+1:
                end = nums[ni]
            else:
                if start == end:
                    answer.append(f"{start}")
                else:
                    answer.append(f"{start}->{end}")
                start = nums[ni]
                end = nums[ni]
        if start == end:
            answer.append(f"{start}")
        else:
            answer.append(f"{start}->{end}")
        return answer
