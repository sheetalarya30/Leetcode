class Solution:
    def maxPower(self, s: str) -> int:
        count,ans=1,1
        N=len(s)
        for i in range(0,N-1):
            if s[i]==s[i+1]:
                count+=1
            else:
                count=1
            ans=max(ans,count)
        return ans