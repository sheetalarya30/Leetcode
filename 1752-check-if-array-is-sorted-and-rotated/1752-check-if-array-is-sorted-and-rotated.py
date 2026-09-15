class Solution(object):

    def check(self, a):

        count=0

        for i in range(0,len(a)):

            if a[i]>a[(i+1)%len(a)]:

                count+=1

        if(count<=1):

            return True

        return False