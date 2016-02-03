def main():
    n = input()
    if n <= 3:
        return True
    if n == 4:
        return False
    if n >= 5:
        if ((n - 5) % 4) <= 2:
            return True
        else:
            return False


result = main()
print result