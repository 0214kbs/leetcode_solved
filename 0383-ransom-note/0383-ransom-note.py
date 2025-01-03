class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ri = 0
        for mi in range(len(magazine)):
            if magazine[mi] == ransomNote[ri]:
                ri +=1 
                if len(ransomNote) == ri: return True # over
            else:
                ri = 0
        return False
