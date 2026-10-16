class Solution:
    def isHappy(self, n: int) -> bool:
        numSet = set()
        while n != 1:
            if n in numSet:
                return False
            numSet.add(n)
            digSum = 0
            while n > 0:
                digSum += (n % 10) ** 2
                n //= 10
            n = digSum
        return True
