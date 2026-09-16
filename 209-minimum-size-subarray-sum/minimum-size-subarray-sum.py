class Solution(object):
    def minSubArrayLen(self, target, nums):
        left=0
        right=0
        summ=0
        min_len=float('inf')
        while right<len(nums):
            summ+=nums[right]
            while summ>=target:
                length=right-left+1
                min_len=min(min_len,length)
                summ-=nums[left]
                left+=1
            right+=1
        return min_len if min_len!=float('inf') else 0


       
        