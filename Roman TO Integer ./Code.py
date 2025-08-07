class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

        total = 0
        prev_value = 0

        for char in reversed(s):  # Traverse from right to left
            current_value = roman_map[char]
            if current_value < prev_value:
                total -= current_value  # Subtract if smaller value comes before a larger one
            else:
                total += current_value  # Add otherwise
            prev_value = current_value

        return total
        
