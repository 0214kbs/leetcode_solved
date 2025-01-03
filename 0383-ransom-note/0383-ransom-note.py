class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        check = {}
        for m in magazine:
            if m in check:
                check[m] +=1
            else: check[m] = 1
        for r in ransomNote:
            if r in check:
                check[r] -= 1
                if check[r] < 0: return False
            else: return False
        return True