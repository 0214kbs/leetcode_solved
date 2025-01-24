class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = [0 for _ in range(len(boxes))]

        for bi in range(len(boxes)):
            if boxes[bi] == "1":
                l, r = bi-1, bi+1
                add = 1
                while True:
                    if l<0 and r>=len(boxes):
                        break
                    if l>=0:
                        res[l] += add
                    if r< len(boxes):
                        res[r] += add
                    l ,r = l-1, r+1
                    add +=1
        return res