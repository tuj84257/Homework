# This file contains the necessary data structures 
# and methods needed to complete this project

from utils import hash_function                                                                                                 # import the hash function

# Class that stores the original key, as well as
# the same key converted to a string (this class
# will be useful for alphabetically-sorting the
# keys)
class key:
    def __init__(self, key):
        self.key_original_type = key                                                                                            # the original key
        self.key_as_string = str(key)                                                                                           # the key converted to string

# Class that defines a linked list node
class node:
    def __init__(self, data, next=None, index_in_list=0):
        self.data = data                                                                                                        # the key or value given by the user
        self.next = next                                                                                                        # pointer to the next node in the list

# Class that defines a linked list   
class linkedList:
    def __init__(self, head=None):
        self.head = head                                                                                                        # the head of the linked list (points to None by default)
    
    # method that prints the linked list
    # (can be used to check the contents of 
    # the linked list for testing purposes)    
    def printList(self):
        currNode = self.head                                                                                                    # start by pointing to the head of the linked list                                                           
        while currNode is not None:                                                                                             # as long as the end of the linked list has not been reached                                                        
            if currNode.next is None:                                                               
                print(currNode.data, end="")                                                                                    #   print the key or value stored in the current node       
            else:
                print(currNode.data, end=" -> ")
            currNode = currNode.next                                                                                            # move to the next node                          
        print()
        
    # method that appends a node to the
    # linked list
    def add(self, data):
        newNode = node(data)                                                                                                    # create a new node                                            
        tail = self.head                                                                                                        # start from the head of the linked list
        if self.head == None:                                                                                                   # if head points to None, that means the list is empty                                                                                                  
            self.head = newNode                                                                                                 #   therefore, make head point to the new node
        else:                                                                                                                   # else
            while tail.next != None:                                                                                            #   traverse to the tail of the linked list
                tail = tail.next
            tail.next = newNode                                                                                                 #   and append the new node
    
    # method that finds a node in the
    # linked list, given the data it stores        
    def find(self, data):
        currNode = self.head                                                                                                    # start from the head of the linked list
        n = 0                                                                                                                   # use this variable to extract the index of the node in the linked list
        while currNode is not None:                                                                                             # as long as the end of the linked list has not been reached                       
            if currNode.data == data:                                                                                           #   if the current node contains data that matches the given information
                return [currNode, n]                                                                                            #     return the node and its index in the linked list                                         
            currNode = currNode.next                                                                                            #   move to the next node
            n += 1                                                                                                              #   increment the index variable
        return None                                                                                                             # return None if the node was not found

# Class that defines the dictionary            
class dictionary:
    def __init__(self, size=10):                                                                                                # the default size of the arrays of keys and values is 10
        self.keys = []                                                                                                          # the array of keys
        self.values = []                                                                                                        # the array of values
        self.size = size                                                                                                        # the size of the dictionary (which is the size of the arrays)
        self.length = 0                                                                                                         # the number of key-value pairs
        for i in range(size):
            self.keys.append(linkedList())                                                                                      # fill both arrays with linked list objects to handle collisions
            self.values.append(linkedList())            
    
    # method that inserts a key-value pair into 
    # the dictionary (the user can use this method
    # or the __setitem__ one to insert data into
    # the dictionary)
    def insert(self, key, value):
        index = hash_function(key, self.size)                                                                                   # calculate the array index from the hash function
        if self.keys[index].find(key) is not None:                                                                              # make sure the key the user is adding is unique, or else raise a key error
            raise KeyError("ERROR: The key could not be added because it already exists in the dictionary!")
        self.keys[index].add(key)                                                                                               # add the given key to the array of keys
        self.values[index].add(value)                                                                                           # add the given value to the array of values
        self.length += 1                                                                                                        # increment the length of the dictionary
    
    # method that returns a value from the dictionary
    # for a given key (the user can use this method,
    # or the __getitem__ one to get data from
    # the dictionary)
    def get(self, key):
        index = hash_function(key, self.size)                                                                                   # calculate the array index from the hash function
        result = self.keys[index].find(key)                                                                                     # go to that index in the array of keys, and find the linked list node that holds the given key
        if result is None:                                                                                                      # if the result is None
            raise KeyError(                                                                                                     #   this means the given key is not in the dictionary; thus, raise a key error
                "ERROR: The value could not be retrieved because the given key does not exist in the dictionary!"
            )
        node_with_the_key, node_index = result                                                                                  # extract the node and the index of the node inside the linked list
        currNode = self.values[index].head                                                                                      # go to the head of the linked list that is located at the same index in the array of values
        n = 0                                                                                                                   # use `n` to get the index of the linked list node that holds the value in the array of values, and check whether it matches the index of the node that holds the key in the array of keys
        while n != node_index:                                                                                                  # as long as the index of the node in the linked list of the array of values is not the same as the index of the node in the linked list of the array of keys
            currNode = currNode.next                                                                                            #   move to the next node in the linked list
            n += 1                                                                                                              #   increment `n`
        return currNode.data                                                                                                    # when you find the node, return the value that it holds
    
    # built-in method, used here to insert a key-value 
    # pair into the dictionary
    def __setitem__(self, key, value):
        self.insert(key, value)
    
    # built-in method, used here to get a value from
    # the dictionary for a given key
    def __getitem__(self, key):
        return self.get(key)
    
    # method that prints the dictionary for each
    # array index, or in alphabetical order
    def display(self, sorted_alphabetically=False):
        if sorted_alphabetically is False:                                                                                      # if the user does not want to sort the items in alphabetical order
            i = -1                                                                                                              #   use this variable to keep track of the array index
            for keys_list in self.keys:                                                                                         #   for each linked list in the array of keys
                i += 1
                if keys_list.head is None:                                                                                      #     if the linked list is empty
                    pass                                                                                                        #       ignore it
                else:                                                                                                           #     else
                    currNode = keys_list.head                                                                                   #       start from the head of the linked list
                    print('At index', i, 'the dictionary contains:', end=" {")
                    while currNode is not None:
                        if currNode.next is None:
                            print(str(repr(currNode.data)) + ':', repr(self[currNode.data]), end="")                            #       and print the key-value pairs by preserving the Python dictionary format
                        else:                                                                                                   #       (I used `repr` to print the variables the same way as they're printed in a python dictionary - for example a string is printed with single quotes)
                            print(str(repr(currNode.data)) + ':', repr(self[currNode.data]), end=", ")
                        currNode = currNode.next
                    print("}")
        elif sorted_alphabetically is True:                                                                                     # else, if the user wants to sort the items in alphabetical order
            all_keys = []                                                                                                       #   initialize `all_keys` as an empty array (use it to later store all `key` objects here)
            for keys_list in self.keys:                                                                                         #   for each linked list in the `keys` array
                if keys_list.head is None:                                                                                      #     if the list is empty
                    pass                                                                                                        #       ignore it
                else:                                                                                                           #     else
                    currNode = keys_list.head                                                                                   #       start from the head of the linked list
                    while currNode is not None:                                                                                 #       as long as the end of the list has not been reached
                        all_keys.append(key(currNode.data))                                                                     #         create a `key` object using the key stored in the current node, and append the object to `all_keys`
                        currNode = currNode.next                                                                                #         move to the next node
            all_keys = sorted(sorted(all_keys, key=lambda x: x.key_as_string), key=lambda x: x.key_as_string.casefold())        #   sort the objects based on the string attribute (`casefold()` makes sure that the uppercase letter comes before the lowercase one)
            print('{', end="")
            for key_object in all_keys:                                                                                         #   for each `key` object in the `all_keys` array
                if key_object == all_keys[-1]:
                    print(str(repr(key_object.key_original_type)) + ':', repr(self[key_object.key_original_type]), end="}")     #     print the attribute that stores the original key type by preserving Python's dictionary format 
                else:    
                    print(str(repr(key_object.key_original_type)) + ':', repr(self[key_object.key_original_type]), end=", ")
            print()        
        else:                                                                                                                   # else
            raise ValueError("ERROR: The input argument must be explicitly specified as True or False!")                        #   raise value error if the input argument is not True or False
    
    # built-in method to print the dictionary
    # in the classical Python fashion
    def __str__(self):
        myString = '{'                                                                                                          # the string that represents the contents of the dictionary
        pair_index = 0                                                                                                          # use this variable to keep track of the index of the key-value pairs in the dictionary
        for keys_list in self.keys:                                                                                             # for each linked list in the array of keys
            if keys_list.head is None:                                                                                          #   if the linked list is empty
                pass                                                                                                            #     ignore it
            else:                                                                                                               #   else
                currNode = keys_list.head                                                                                       #     start from the head of the linked list
                while currNode is not None:                                                                                     #     as long as the end of the list has not been reached
                    if pair_index == self.length - 1:                                                                           #       check whether you've arrived at the last (key, value) pair in the dictionary
                        myString += str(repr(currNode.data)) + ": " + repr(self[currNode.data])                                 #       and add the key-value pairs accordingly to `myString`
                    else:    
                        myString += str(repr(currNode.data)) + ": " + repr(self[currNode.data]) + ", "
                    currNode = currNode.next                                                                                    #       move to the next node
                    pair_index += 1                                                                                             #       increment the key-value pair index
        myString += '}'
        return myString                                                                                                         # return `myString`
        