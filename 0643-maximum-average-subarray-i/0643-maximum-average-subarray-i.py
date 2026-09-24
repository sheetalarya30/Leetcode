class Solution:
    def findMaxAverage(self, a: list[int], k: int) -> float:
        wsum=sum(a[0:k])
        maxs=wsum
        for i in range(k,len(a)):
            wsum=wsum+a[i]-a[i-k]
            maxs=max(wsum,maxs)
        return maxs/k