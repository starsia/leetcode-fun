class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def bananas(speed):
            return sum(math.ceil(pile/speed) for pile in piles) <= h

        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if bananas(mid):
                r = mid
            else:
                l = mid + 1

        return l 
                
