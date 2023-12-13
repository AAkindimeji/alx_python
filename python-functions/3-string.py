def reverse_string(string):
    return string[::-1]
reverse_string = __import__('3-string').reverse_string
print(reverse_string("Hello"))
print(reverse_string(""))
print(reverse_string("madam"))
print(reverse_string("Hello, World!"))

# def reverse_string(string):
#     return string[::-1]

# strings = ["Hello", "", "madam", "Hello, World!"]

# for string in strings:
#     print(reverse_string(string))
