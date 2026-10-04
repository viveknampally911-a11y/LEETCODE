class Solution(object):
    def sortedSquares(self, nums):
        op=[]
        for i in nums:
            op.append(i**2)
        op.sort()
        return op
        