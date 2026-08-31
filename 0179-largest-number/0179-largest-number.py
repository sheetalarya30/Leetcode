class Solution:
    def largestNumber(self, arr: List[int]) -> str:
       n=len(arr)
       arr=list(map(str,arr))
       for i in range(n):
         for j in range(i+1,n):
            if arr[i]+arr[j]<arr[j]+arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
       if arr[0]=="0":
            return "0"
       return "".join(arr)