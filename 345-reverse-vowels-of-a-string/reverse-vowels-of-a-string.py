class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        l=0
        r=len(s)-1

        while l<r:
            if s[l] not in "AEIOUaeiou":
                l+=1
                continue

            if s[r] not in "AEIOUaeiou":
                r-=1
                continue

            temp=s[l]
            s[l]=s[r]
            s[r]=temp

            l+=1
            r-=1

        return "".join(s)