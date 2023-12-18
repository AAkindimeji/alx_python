def inherits_from(obj, a_class):
    """Check if obj is an instance of a class inherited from the specified class."""
    return issubclass(type(obj), a_class)

# Test the function
# a = True
# if inherits_from(a, int):
#     print("{} inherited from class {}".format(a, int.__name__))
# if inherits_from(a, bool):
#     print("{} inherited from class {}".format(a, bool.__name__))
# if inherits_from(a, object):
#     print("{} inherited from class {}".format(a, object.__name__))
