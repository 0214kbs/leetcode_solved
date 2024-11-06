class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        for b in str(bin(n))[2:]:
            if b == '1':
                answer += 1
        return answer