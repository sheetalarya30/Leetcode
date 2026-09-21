class Solution(object):

    def findMaxAverage(self, a, k):
        wsum=sum(a[0:k])
        maxS=wsum
        for i in range(k,len(a)):
            wsum=wsum+a[i]
            wsum=wsum-a[i-k]
            maxS=max(wsum,maxS)
        return maxS/k
        