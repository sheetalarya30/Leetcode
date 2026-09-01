class Solution:
    def countAndSay(self, n: int) -> str:
        cur = "1"
        for _ in range(n-1):
            next = ""
            count = 1
            N = len(cur)
            for i in range(1, N):
                if cur[i] == cur[i-1]:
                    count += 1
                else:
                    next += str(count) + str(cur[i-1])
                    count = 1
            next += str(count) + str(cur[N-1])
            cur = next
        return cur