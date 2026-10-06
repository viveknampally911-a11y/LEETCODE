# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        l=0
        r=n
        while l<=r:
            ans=(l+r)//2
            if guess(ans)==-1:
                r=ans-1
            elif guess(ans)==0:
                return ans
            else:
                l=ans+1
