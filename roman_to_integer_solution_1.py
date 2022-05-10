class Solution:

    def __init__(self):
        self.roman_symbol_int_value_map = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

    def subtract_largest_to_smaller_number(self, left_side_letter, right_side_letter):
        return self.roman_symbol_int_value_map[right_side_letter] - \
            self.roman_symbol_int_value_map[left_side_letter]

    def romanToInt(self, s: str) -> int:
        """
           Roman to integer
           M+CM+XC+IV --- 1000 + (100-1000) + (10-100) + (1-5)
                      --- 1000 + 900 + 90 + 4
                      --- 1994
        """
        sum = 0
        total_length = len(s)
        i = 0
        while i < total_length:
            if i < total_length - 1:
                if (s[i] == 'I' and (s[i+1] == 'V' or s[i+1] == 'X')) or \
                    (s[i] == 'X' and (s[i+1] == 'L' or s[i+1] == 'C')) or \
                        (s[i] == 'C' and (s[i+1] == 'D' or s[i+1] == 'M')):
                    sum += self.subtract_largest_to_smaller_number(
                        s[i], s[i+1])
                    i = i + 2
                    continue
            sum += self.roman_symbol_int_value_map[s[i]]
            i = i + 1
        return sum


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('MCMXCIV'))
