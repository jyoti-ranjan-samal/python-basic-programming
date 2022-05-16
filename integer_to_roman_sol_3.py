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
        print("Hello")
        roman_number = ''
        if num >= 1000:
            multiple = num // 1000
            roman_number += self.roman_symbol_value[1000] * multiple
            num -= (multiple * 1000)

        if num >= 100:
            if num == 100:
                roman_number += self.roman_symbol_value[100]
                num -= 100
            elif num == 900:
                roman_number += self.roman_symbol_value[900]
                num -= 900
            elif num == 400:
                roman_number += self.roman_symbol_value[400]
                num -= 400
            elif num == 500:
                roman_number += self.roman_symbol_value[500]
                num -= 500
            else:
                multiple = num // 100
                roman_number += self.roman_symbol_value[100] * multiple
                num -= (multiple * 100)

        if num >= 10:
            if num == 10:
                roman_number += self.roman_symbol_value[10]
                num -= 10
            elif num == 40:
                roman_number += self.roman_symbol_value[40]
                num -= 40
            elif num == 50:
                roman_number += self.roman_symbol_value[50]
                num -= 50
            else:
                multiple = num // 10
                roman_number += self.roman_symbol_value[10] * multiple
                num -= (multiple * 10)

        if num == 1:
            roman_number += self.roman_symbol_value[1]
        elif num == 4:
            roman_number += self.roman_symbol_value[40]
        elif num == 5:
            roman_number += self.roman_symbol_value[5]
        else:
            print(f"{num}")
            multiple = num // 1
            roman_number += self.roman_symbol_value[1] * multiple
        return roman_number


s = Solution()
print(s.intToRoman(3))
