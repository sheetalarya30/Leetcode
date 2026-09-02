class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        N = len(heights)
        #expected = heights --> why this will not work?
        expected = heights[0:N]
        expected.sort()
        count = 0
        for i in range(0, N):
            if expected[i] != heights[i]:
                count += 1
        return count
        