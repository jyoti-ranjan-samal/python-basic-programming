def reverse_number(n, rev_num=0):
    if n == 0:
        return rev_num
    else:
        rev_num = rev_num * 10 + n % 10
        return reverse_number(n//10, rev_num)


if __name__ == '__main__':
    print(reverse_number(1234567))
