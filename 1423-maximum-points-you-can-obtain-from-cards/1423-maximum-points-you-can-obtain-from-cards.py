class Solution(object):
    def maxScore(self, a, p):
        n=len(a)
        if p==n:
            return sum(a)
        k=n-p
        wsum=sum(a[0:k])
        minS=wsum
        for i in range(k,n):
            wsum+=a[i]
            wsum-=a[i-k]
            minS=min(wsum,minS)
        return sum(a)-minS
        