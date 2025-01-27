class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        check = {}
        for i in range(len(s)):
            if s[i] in check:
                if check[s[i]] != t[i]:
                    return False
            else:
                check[s[i]] = t[i]
        
        return True 