class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        sumprev = 1
        for i in range(2, n):
            dp[i] += (dp[i-1] + dp[i-2] + sumprev*2) % (10**9+7)
            sumprev += dp[i-2]
        return dp[n-1]
