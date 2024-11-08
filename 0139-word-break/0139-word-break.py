class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for end in range(1, len(s)+1):
            for word in wordDict:
                if end-len(word)>=0 and s[end-len(word) : end] == word:
                    dp[end] = dp[end-len(word)]
                if dp[end]: break
        return dp[-1]


