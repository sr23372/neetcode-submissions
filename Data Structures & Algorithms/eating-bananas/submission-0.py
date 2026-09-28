import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        res = R
        while L <= R:
            middle = (R + L) // 2
            totalTime = 0
            for nums in piles:
                totalTime += math.ceil(float(nums) / middle)
            
            if totalTime <= h:
                res = middle
                R = middle - 1
            else: 
                L = middle + 1
        return res




        