class Solution(object):
    def minEatingSpeed(self, a, h):
        left=1
        right=max(a)
        while left<=right:
            mid=(left+right)//2
            hours=0
            for n in a:
                hours+=math.ceil(n/mid)
            if hours<=h:
                right=mid-1
            else:
                left=mid+1
        return left
        