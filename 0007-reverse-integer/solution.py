class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        n = 0
        rev = 0
        while x > 0:
            n = x % 10
            rev = rev * 10 + n
            x = x // 10
        rev *= sign
        return rev if -2**31 <= rev <= 2**31 -1 else 0
