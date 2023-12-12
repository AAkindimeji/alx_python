def no_c(my_string):
    # Use list comprehension to create a new string without 'c' and 'C'
    new_string = ''.join(char for char in my_string if char not in ('c', 'C'))
    return new_string

# Test cases
print(no_c("Holberton School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
