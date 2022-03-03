n1, n2 = 0, 1


def fibonacci(n1, n2, count=0, first=True, terms=10):
    if first:
        print(n1)
    print(n2)
    next_num = n1 + n2
    n1 = n2
    n2 = next_num
    count += 1
    if count != terms:
        fibonacci(n1, n2, count, False)


fibonacci(n1, n2)
