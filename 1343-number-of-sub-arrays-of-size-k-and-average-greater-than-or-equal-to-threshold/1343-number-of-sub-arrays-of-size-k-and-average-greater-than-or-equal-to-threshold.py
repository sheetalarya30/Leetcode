class Solution:
    def numOfSubarrays(self, a: list[int], k: int, threshold: int) -> int:
        count=0
        wsum=sum(a[0:k])
        if wsum>=threshold*k:
           count+=1
        for i in range(k,len(a)):
            wsum=wsum+a[i]-a[i-k]
            if wsum>=threshold*k:
               count+=1
        return count


