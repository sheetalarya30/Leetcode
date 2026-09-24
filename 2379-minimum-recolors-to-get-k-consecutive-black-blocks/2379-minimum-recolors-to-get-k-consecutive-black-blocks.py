class Solution:
    def minimumRecolors(self, s,k):
        count=0
        for i in range(0,k):
            if s[i]=='W':
                count+=1
        minW=count
        for i in range(k,len(s)):
            if s[i]=='W':
                count+=1
            if s[i-k]=="W":
                count-=1
            minW=min(count,minW)
        return minW