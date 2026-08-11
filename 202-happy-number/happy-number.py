class Solution:
    def isHappy(self, n: int) -> bool:
        def next_number(x):
            total = 0
            while x > 0:
                digit = x % 10
                total += digit * digit
                x //= 10
            return total
        
        s= set()
        while n != 1 and n not in s:
            s.add(n)
            n = next_number(n)
        
        return n == 1
