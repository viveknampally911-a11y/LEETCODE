class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxi = 0
        r = []

        for i in range(len(s)):
            if s[i] not in r:
                r.append(s[i])
            else:
                while s[i] in r:
                    r.pop(0)
                r.append(s[i])

            maxi = max(maxi, len(r))

        return maxi