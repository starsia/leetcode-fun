class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = 0
        n = len(s)
        
        if n <= 1:
            return s
            
        output = ""
        
        for i in range(n):
            bef = i
            aft = i
            # odd
            while bef >= 0 and aft < n and s[bef] == s[aft]:
                if aft - bef + 1 > count:
                    output = s[bef:aft + 1]
                    count = aft - bef + 1
                    
                
                bef -= 1
                aft += 1
            
            bef = i 
            aft = i + 1
            
            while bef >= 0 and aft <n and s[bef] == s[aft]:
                if aft - bef + 1 > count:
                    output = s[bef:aft+1]
                    count = aft-bef+1
                    
                bef -= 1
                aft += 1
            
        return output
            
