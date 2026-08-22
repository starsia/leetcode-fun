class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1

            substring.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

            
