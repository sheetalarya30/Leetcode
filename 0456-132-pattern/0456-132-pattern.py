class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float('-inf')  # this represents the "2" in "132", best candidate so far

        for num in reversed(nums):
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()   # pop smaller elements, they become potential "2"
            stack.append(num)

        return False
