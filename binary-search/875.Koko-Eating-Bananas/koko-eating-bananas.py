class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def bananas(speed):
            return sum(math.ceil(pile/speed) for pile in piles) >= H

        l, r = 1, len(piles)
        while l < r:
            mid = (l + r) // 2
            if bananas(mid):
                return mid
            elif 
