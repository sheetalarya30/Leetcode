class Solution(object):
    def maxVowels(self, s, k):
        vowels="aeiou"
        count=0
        for i in range(0,k):
            if s[i] in vowels:
                count+=1
        maxV=count
        for i in range(k,len(s)):
            if s[i] in vowels:
                count+=1
            if s[i-k] in vowels:
                count-=1
            maxV=max(count,maxV)
        return maxV
        