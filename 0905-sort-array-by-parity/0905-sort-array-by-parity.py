class Solution(object):

    def sortArrayByParity(self, a):

        n=len(a)

        left=0

        right=n-1

        while(left<right):

            while(left<right and a[left]%2==0):

                left+=1

            while(left<right and a[right]%2==1):

                right-=1

            if(left<right):

                a[left],a[right]=a[right],a[left]

        return a
        