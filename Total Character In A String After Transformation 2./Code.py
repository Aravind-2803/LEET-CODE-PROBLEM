class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        # Step 1: Initialize the frequency of each character in the input string
        curr_freq = [0] * 26
        for ch in s:
            curr_freq[ord(ch) - ord('a')] += 1
        # Step 2: Perform t transformations
        for _ in range(t):
            new_freq = [0] * 26
            for i in range(26):  # for each character from 'a' to 'z'
                freq = curr_freq[i]
                if freq == 0:
                    continue
                # Each character generates nums[i] new characters
                for j in range(1, nums[i] + 1):
                    new_index = (i + j) % 26  # wrap around using modulo
                    new_freq[new_index] = (new_freq[new_index] + freq) % MOD
            curr_freq = new_freq
        # Step 3: Calculate total length after all transformations
        return sum(curr_freq) % MOD
