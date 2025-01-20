class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        check = [0 for _ in range(len(triangle[-1]))]
        for d in range(len(triangle)-1, 0,-1):
            nxt = []
            for i in range(len(triangle[d])-1):
                nxt.append(min(triangle[d][i]+check[i],triangle[d][i+1]+check[i+1]))
            check = nxt
        return check[0]+triangle[0][0]