class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        check = {}
        def dfs(start):
            if start in check:
                return check[start]
            if start == len(s):
                return True

            for word in wordDict:
                if s[start:start+len(word)] == word:
                    if dfs(start+len(word)):
                        return True
            check[start] =False
            return False
        return dfs(0)