class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            last = 1
            secondlast = 0
            for _ in range(2,n+1):
                cur = last + secondlast
                secondlast = last
                last = cur
            return last
