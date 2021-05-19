# This file contains the hash function needed to
# calculate the index of the array where the keys
# given by the user will be stored. For each
# allowed key type, there is a respective algorithm
# used to return the index.

# The hash function
def hash_function(key, size_of_array):
    if isinstance(key, int):                                                                                                  # check if the given key is an integer
        return key % size_of_array
    if isinstance(key, float):                                                                                                # check if the given key is a float
        return int(key) % size_of_array
    if isinstance(key, str):                                                                                                  # check if the given key is a string
        sum_of_ordinal_values = 0
        for character in key:
            sum_of_ordinal_values = sum_of_ordinal_values + (ord(character))**2
        return sum_of_ordinal_values % size_of_array
    else:                                                                                                                     # if the given key is not an integer, float, or string
        raise KeyError("Key not allowed! You can only insert keys that are of these data types: int, float or string.")       #   raise error and let the user know about the allowed key types
