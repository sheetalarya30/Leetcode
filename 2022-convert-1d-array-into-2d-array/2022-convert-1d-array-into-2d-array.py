class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        N = len(original)
        if n*m != N:
            return ans
        index = 0
        for i in range(0,m):
            cur = []
            for j in range(0, n):
                cur.append(original[index])
                index += 1
            ans.append(cur)
        return ans
        