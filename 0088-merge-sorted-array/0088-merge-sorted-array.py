import copy
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0: return
        cur = 0

        remain = 0
        for i in range(len(nums1)):
            if cur >= n: 
                remain +=1
                continue
            if nums1[i] == 0:
                nums1[i] = nums2[cur]
                cur+=1
        nums1.sort()
        nums1 = nums1[remain:]
        