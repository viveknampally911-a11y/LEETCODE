class Solution(object):
    def isHappy(self, n):
        if n == 1:
            return True

        if n == 4:
            return False

        total = 0

        while n > 0:
            digit = n % 10
            total += digit ** 2
            n = n // 10

        return self.isHappy(total)