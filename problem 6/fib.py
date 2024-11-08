# Adam Dyer
# Friday Lab

def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        (prev, current) = (0, 1)
        for x in range(2, n + 1):
            (prev, current) = (current, prev + current)
        return current

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')