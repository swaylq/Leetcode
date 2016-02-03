def main():
    n = input()
    if n == 0:
        return 0
        
    if n % 9 == 0:
        return 9
    else:
        return n % 9

result = main()
print result