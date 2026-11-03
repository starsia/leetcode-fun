class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        
        for s in strs:
            arr = [0] * 26
            
            for c in s:
                arr[ord(c) - 97] += 1
            
            d[tuple(arr)].append(s)
            
        return list(d.values())
