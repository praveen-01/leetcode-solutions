import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def bananas_eat(k):
            time = 0
            for i in piles:
                time+=math.ceil(i/k)
            return time
        i = 1
        j = max(piles)
        ans = 0
        while i<=j:
            mid = (i+j)//2
            time_taken = bananas_eat(mid)
            if time_taken<=h:
                ans = mid
                j = mid-1
            else:
                i = mid+1
        return ans
        