class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        We know how to generate all substring
        We just check each substring is panlindrome or not
        and return longest (panlindrome) substring
        """
        N = len(s)
        def isPanlindrome(start, end):
            flag = True
            while start < end:
                if s[start] != s[end]:
                    flag = False
                    break
                start += 1
                end -= 1
            return flag
        ans = ""
        for i in range(0, N):
            for j in range(i, N):
                if len(ans) < (j-i+1) and isPanlindrome(i,j):
                    ans = s[i:j+1]
        return ans