from math import log10, floor


from math import log10, floor


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

    def get_number_of_digits(self, num):
        return floor(log10(num) + 1)

    def intToRoman(self, num: int) -> str:
        roman_number = ''
        total_num_of_digits = self.get_number_of_digits(num)
        while total_num_of_digits > 0 and num > 0:
            position = pow(10, total_num_of_digits-1)
            face_value_of_num = num // position
            place_value_of_number = face_value_of_num * position

            if self.roman_symbol_value.get(place_value_of_number):
                roman_number += self.roman_symbol_value[place_value_of_number]
            else:
                place_value_of_number_2 = place_value_of_number
                if position == 1000:
                    a = [1000]
                    for ele in a:
                        if place_value_of_number_2 >= ele:
                            roman_number += self.roman_symbol_value[ele] * \
                                (place_value_of_number_2 // ele)
                            place_value_of_number_2 -= ele
                elif position == 100:
                    a = [500, 100]
                    for ele in a:
                        if place_value_of_number_2 >= ele:
                            roman_number += self.roman_symbol_value[ele] * \
                                (place_value_of_number_2 // ele)
                            place_value_of_number_2 -= ele

                elif position == 10:
                    a = [50, 10]
                    for ele in a:
                        if place_value_of_number_2 >= ele:
                            roman_number += self.roman_symbol_value[ele] * \
                                (place_value_of_number_2 // ele)
                            place_value_of_number_2 -= ele

                elif position == 1:
                    a = [5, 1]
                    for ele in a:
                        if place_value_of_number_2 >= ele:
                            roman_number += self.roman_symbol_value[ele] * \
                                (place_value_of_number_2 // ele)
                            place_value_of_number_2 -= ele

            num = num - place_value_of_number
            total_num_of_digits -= 1
        return roman_number


s = Solution()
print(s.intToRoman(2000))
