class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        N1,N2,N3=len(s1),len(s2),len(s3)
        N=min(N1,N2,N3)
        finallength=0
        for i in range(0,N):
            if s1[i]==s2[i] and s2[i]==s3[i]:
                finallength+=1
            else:
                break
        if finallength==0:
            return -1
        ans = N1-finallength
        ans+= N2-finallength
        ans+= N3-finallength
        return ans