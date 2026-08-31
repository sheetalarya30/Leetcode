class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == 'b' and s[j] == 'a':
                    return False

        return True
        
        # return "ba" not in s