class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        """
        We generate all subarrays, and then we will check
        each subarray is valid or not
        """
        count = 0
        def isValid(start, end):
            flag = True
            check = nums[start+1] - nums[start]
            for i in range(start+1, end+1):
                if nums[i] - nums[i-1] != check:
                    flag = False
                    break
            return flag

        for i in range(0, N):
            #i = 0, j = 2 --> [0,1,2]
            for j in range(i+2,N):
                if isValid(i, j):
                    count += 1
        return count
        