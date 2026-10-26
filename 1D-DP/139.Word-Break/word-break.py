class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        memo = [False] * (len(s) + 1)
        memo[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    memo[i] = memo[i + len(word)]

                    if memo[i] == True:
                        break

        return memo[0]

