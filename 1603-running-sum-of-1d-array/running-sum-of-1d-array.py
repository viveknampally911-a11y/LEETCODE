class Solution(object):
    def runningSum(self, nums):
        run=[]
        s=nums[0]
        run.append(nums[0])
        for i in range(1,len(nums)):
            s+=nums[i]
            run.append(s)
        return run

            
        