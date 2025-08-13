class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        elif n < 0:
            n -= 1
            n = abs(n)
        while n > 1:
            if n % 3 != 0:
                return False
            n /= 3
        return True