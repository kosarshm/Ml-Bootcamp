def my_multiple(x, y):
    i = 0
    sum = 0
    while i < y:
        sum += x
        i += 1
    return sum


x = int(input())
y = int(input())
print(my_multiple(x, y))
