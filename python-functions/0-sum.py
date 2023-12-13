#!/usr/bin/python3

def add(a, b):
    return a + b
add = __import__('0-sum').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))


# def add(a, b):
#     return a + b

# pairs = [(1, 2), (98, 0), (100, -2)]

# for pair in pairs:
#     print(add(*pair))
