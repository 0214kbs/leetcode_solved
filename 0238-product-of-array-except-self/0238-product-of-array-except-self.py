class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productAllExceptZero = 1
        zero_cnt = 0
        for n in nums:
            if n==0:
                zero_cnt +=1
            else:
                productAllExceptZero*=n

        answer = []
        for n in nums:
            if n == 0:
                if (zero_cnt -1) > 0: answer.append(0)
                else: answer.append(productAllExceptZero)
            else:
                if zero_cnt > 0:
                    answer.append(0)
                else:
                    answer.append(productAllExceptZero//n)
        return answer