class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False for _ in range(len(s))]
        for i in range(1, len(s)+1):
            for word in wordDict:
                if s[i-len(word):i] == word:
                    dp[i] = dp[i-len(word)]
                if dp[i]:
                    break
        return dp[-1]