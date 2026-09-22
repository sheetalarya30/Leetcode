class Solution(object):

    def minSubArrayLen(self, target, a):

        i=0

        wsum=0

        minlen=float('inf')

        for j in range(0,len(a)):

            wsum=wsum+a[j]

            while(wsum>=target):

                minlen=min(minlen,j-i+1)

                wsum=wsum-a[i]

                i+=1

        if(minlen==float('inf')):

            return 0

        return minlen