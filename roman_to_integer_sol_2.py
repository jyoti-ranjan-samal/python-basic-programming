class Solution:
    def __init__(self):
        self.roman_symbol_value_map = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

    def romanToInt(self, s: str) -> int:
        sum = 0
        prev_sum = 0
        curr = prev = self.roman_symbol_value_map[s[0]]
        for i in range(len(s)):
            curr = self.roman_symbol_value_map[s[i]]
            if prev < curr:
                prev_sum += 2 * prev
            prev = curr
            sum += curr
        return sum - prev_sum


s = Solution()
print(s.romanToInt('MCMXCIV'))
