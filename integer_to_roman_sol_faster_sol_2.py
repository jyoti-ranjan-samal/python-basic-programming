class Solution:

    def __init__(self) -> None:
        self.roman_symbol_value = {
            1: 'I', 5: 'V',
            10: 'X', 50: 'L',
            100: 'C', 500: 'D',
            1000: 'M', 400: 'CD',
            900: 'CM',
            4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC'
        }

    def intToRoman(self, num: int) -> str:
        roman_number = ''
        if num >= 1000:
            multiple = num // 1000
            roman_number += self.roman_symbol_value[1000] * multiple
            num -= (multiple * 1000)
        if num >= 100:
            multiple = num // 100
            actual_number = multiple * 100
            direct_symbol = self.roman_symbol_value.get(actual_number)
            if direct_symbol is not None:
                roman_number += direct_symbol
                num -= actual_number
            else:
                if actual_number >= 500:
                    roman_number += self.roman_symbol_value.get(500)
                    num -= 500

                multiple = num // 100
                roman_number += self.roman_symbol_value.get(
                    100) * multiple
                num -= multiple * 100
        if num >= 10:
            multiple = num // 10
            actual_number = multiple * 10
            direct_symbol = self.roman_symbol_value.get(actual_number)
            if direct_symbol is not None:
                roman_number += direct_symbol
                num -= actual_number
            else:
                if actual_number >= 50:
                    roman_number += self.roman_symbol_value.get(50)
                    num -= 50

                multiple = num // 10
                roman_number += self.roman_symbol_value.get(
                    10) * multiple
                num -= multiple * 10

        direct_symbol = self.roman_symbol_value.get(num)
        if direct_symbol is not None:
            roman_number += direct_symbol
        else:
            if num > 5:
                roman_number += self.roman_symbol_value[5]
                num -= 5

            multiple = num // 1
            roman_number += self.roman_symbol_value[1] * multiple

        return roman_number


s = Solution()
print(s.intToRoman(60))
