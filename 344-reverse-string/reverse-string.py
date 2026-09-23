class Solution(object):
    def reverseString(self, s):
        rev=[]
        for i in range(len(s)-1,-1,-1):
            rev.append(s[i])
        for i in range(len(rev)):
            s[i]=rev[i]

    