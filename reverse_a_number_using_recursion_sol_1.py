def reverse_number(n):
    # return the number from backward and
    # number of digits in the n
    if n == 0:
        return 0, 0
    else:
        digit = n % 10
        final_num, number_of_digits = reverse_number(n//10)
        return digit * pow(10, number_of_digits) + final_num, number_of_digits+1


if __name__ == '__main__':
    final_num, total_digits = reverse_number(1234567)
    print(final_num)
