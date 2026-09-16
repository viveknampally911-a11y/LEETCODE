class Solution(object):
    def findMaxAverage(self, nums, k):
        left=0
        right=0
        summ=0
        avg=0
        max_avg=float('-inf')
        while right<len(nums):
            summ+=nums[right]
            avg=float(summ)/k
            if right-left+1==k:
                summ-=nums[left]
                max_avg=max(max_avg,avg)
                left+=1
            right+=1
        return max_avg

        