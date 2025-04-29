class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        count = 0
        ints = 1
        while ints*(ints-1)/2 < n:
            if (n - ints*(ints-1)/2) % ints == 0:
                count += 1
            ints += 1
        return count
