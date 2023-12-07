def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary."""
    a_dictionary[key] = value
    return a_dictionary

# # Example usage:
# my_dict = {'a': 1, 'b': 2, 'c': 3}

# # Replace existing key
# update_dictionary(my_dict, 'b', 10)
# print(my_dict)  # Output: {'a': 1, 'b': 10, 'c': 3}

# # Add new key
# update_dictionary(my_dict, 'd', 4)
# print(my_dict)  # Output: {'a': 1, 'b': 10, 'c': 3, 'd': 4}
