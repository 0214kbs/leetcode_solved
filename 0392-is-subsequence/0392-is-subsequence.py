class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp, tp = 0,0
        while sp < len(s):
            if tp == len(t):
                return False
            if s[sp] == t[tp]:
                sp+=1
            tp+=1
        if sp == len(s):
            return True
        return False