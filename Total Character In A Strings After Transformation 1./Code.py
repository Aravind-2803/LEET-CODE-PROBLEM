MOD = 10**9 + 7
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        dp = [[0] * 26 for _ in range(t + 1)]
        # Base case: at t=0, each character contributes 1 to the length
        for c in range(26):
            dp[0][c] = 1
        # Fill DP table
        for i in range(1, t + 1):
            for c in range(26):
                if c == 25:  # 'z'
                    # 'z' becomes 'a' and 'b'
                    dp[i][c] = (dp[i-1][0] + dp[i-1][1]) % MOD
                else:
                    # other characters become the next character
                    dp[i][c] = dp[i-1][c + 1] % MOD
        # Calculate total length after t transformations
        result = 0
        for ch in s:
            idx = ord(ch) - ord('a')
            result = (result + dp[t][idx]) % MOD
        return result
