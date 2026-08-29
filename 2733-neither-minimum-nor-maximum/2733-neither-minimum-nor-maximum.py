class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        minV,maxV=nums[0],nums[0]
        for v in nums:
            minV=min(minV,v)
            maxV=max(maxV,v)
        for v in nums:
            if v!= minV and v !=maxV:
                return v
        return -1