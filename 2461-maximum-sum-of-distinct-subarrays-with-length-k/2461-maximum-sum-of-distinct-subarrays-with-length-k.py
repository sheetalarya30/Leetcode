class Solution(object):
    def maximumSubarraySum(self, a, k):
        d={}
        sum=0
        maxS=0
        for i in range(0,k):
            sum=sum+a[i]
            d[a[i]]=d.get(a[i],0)+1
        if len(d)==k:
         maxS=sum
        for i in range(k,len(a)):
            sum=sum+a[i]
            d[a[i]]=d.get(a[i],0)+1
            sum=sum-a[i-k]
            d[a[i-k]]=d[a[i-k]]-1
            if d[a[i-k]]==0:
                del d[a[i-k]]
            if len(d)==k:
                maxS=max(sum,maxS)
        return maxS






        