from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k == len(s):
            return k
        
        count = defaultdict(int)
        left = 0
        max_freq = 0
        answer = 0

        for right in range(len(s)):
            count[s[right]] += 1
            
            for v in count.values():
                max_freq = max(max_freq, v)

            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            answer = max(answer, right - left + 1)



        return answer
