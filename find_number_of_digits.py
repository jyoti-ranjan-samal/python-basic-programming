from math import log10, floor


def number_of_digits(n):
    return floor(int(log10(n))+1)


if __name__ == '__main__':
    print(number_of_digits(123456789123456789))
