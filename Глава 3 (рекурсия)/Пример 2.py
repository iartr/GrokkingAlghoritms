def fact(x: int):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

def factWithCicles(x: int):
    pr = 1
    for i in range(x, 1, -1):
        pr *= i
    return pr

print(fact(5))
print(factWithCicles(5))