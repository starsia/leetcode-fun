class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        l = 0 
        tdict = {} 
        need = len(t) 
        have = {} 
        have_count = 0 
        res, resLen = [-1, -1], float('inf')
        # create maps
        for character in t:
            tdict[character] = 1 + tdict.get(character, 0)
        
        for r in range(len(s)):
            # add element to have dict 
            have[s[r]] = 1 + have.get(s[r], 0)
            
            if s[r] in tdict and have[s[r]] <= tdict[s[r]]:
                have_count += 1

            while need == have_count:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                have[s[l]] -= 1
                if s[l] in tdict and have[s[l]] < tdict[s[l]]:
                    have_count -= 1

                l += 1

        return s[res[0]:res[1] + 1]

