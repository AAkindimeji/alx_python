def pow(a, b):
    return a ** b
pow = __import__('1-power').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

# def pow(a, b):
#     return a ** b

# pairs = [(2, 2), (98, 2), (98, 0), (100, -2), (-4, 5)]

# for pair in pairs:
#     print(pow(*pair))
