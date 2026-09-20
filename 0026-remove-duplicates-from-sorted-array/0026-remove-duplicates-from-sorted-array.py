class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j=0
        n=len(nums)
        for i in range(1,n):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]
        return j+1