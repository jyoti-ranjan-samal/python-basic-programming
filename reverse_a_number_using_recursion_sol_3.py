from math import log10


def reverse_number(n):
    if n == 0:
        return 0
    else:
        return n % 10 * 10 ** int(log10(n)) + reverse_number(n//10)


if __name__ == "__main__":
    print(reverse_number(1234567))
