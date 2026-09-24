class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels="aeiou"
        count=0
        for i in range(0,k):
            if s[i] in vowels:
                count+=1
        maxv=count
        for i in range(k,len(s)):
            if s[i] in vowels:
                count+=1
            if s[i-k] in vowels:
                count-=1
            maxv=max(count,maxv)
        return maxv