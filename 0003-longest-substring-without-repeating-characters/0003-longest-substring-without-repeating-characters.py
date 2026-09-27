class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        needs to find a substring only have unique characters
        it needs to be longest substring

        abca --> valid or not
        """

        # def isValid(start, end):
        #     flag = True
        #     lookUp = set()
        #     for i in range(start, end+1):
        #         if s[i] in lookUp:
        #             flag = False
        #             break
        #         lookUp.add(s[i])
        #     return flag
        # ans = 0
        # N = len(s)
        # for i in range(0,N):
        #     for j in range(i,N):
        #         if isValid(i, j):
        #             if ans < (j-i+1):
        #                 ans = (j-i+1)
        #         else:
        #             break
        # return ans

        win=set()
        i=0
        maxlen=0
        for j in range(0,len(s)):
            while s[j] in win:
                win.remove(s[i])
                i+=1
            win.add(s[j])
            maxlen=max(maxlen,j-i+1)
        return maxlen




