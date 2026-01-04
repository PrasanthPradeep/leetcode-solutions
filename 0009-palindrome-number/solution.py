class Solution:
    def isPalindrome(self, x: int) -> bool:
        sign = -1 if x < 0 else 1
        x = abs(x)
        n = 0
        rev = 0
        y = x
        while x > 0:
            n = x % 10
            rev = rev * 10 + n
            x = x // 10
            rev *= sign
        return rev == y
