class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total=0
        start=0
        tank=0
        for i in range(0,len(gas)):
            total+=gas[i]-cost[i]
            tank+=gas[i]-cost[i]
            if tank<0:
                start=i+1
                tank=0
        if total<0:
            return -1
        return start