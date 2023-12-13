def update_dictionary(a_dictionary, key, value):
    # Update the dictionary with the new key/value pair
    a_dictionary[key] = value
    return a_dictionary

def print_sorted_dictionary(my_dict):
    """Print sorted dictionary."""
    keys = sorted(my_dict.keys())
    for k in keys:
        print("{}: {}".format(k, my_dict[k]))

# # Test cases
# a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }

# # Update an existing key/value pair
# new_dict = update_dictionary(a_dictionary, 'language', "Python")
# print_sorted_dictionary(new_dict)
# print("--")
# print_sorted_dictionary(a_dictionary)

# print("--")
# print("--")

# # Add a new key/value pair
# new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
# print_sorted_dictionary(new_dict)
# print("--")
# print_sorted_dictionary(a_dictionary)
