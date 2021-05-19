from data_structures import dictionary

myDictionary = dictionary()                                                             # Create a dictionary object (you can also define the array size inside the parentheses - by default, it is 10)

myDictionary["Temple"] = 12345                                                          # insert key, value pairs to the dictionary
myDictionary[3822] = "fun"
myDictionary[44.44] = 22.22
myDictionary[53] = "Teddy"
myDictionary["Drexel"] = 34567
myDictionary["ardit"] = 2.4
myDictionary["A"] = 2.4
myDictionary.insert(key="20", value=2.1)                                                # you can also use myDictionary['20'] = 2.1

print('Printing the dictionary:')
myDictionary.display()                                                                  
print('------------------------------------------------------------------------\n')
print('Printing the alphabetically-sorted dictionary:')
myDictionary.display(sorted_alphabetically=True)                                        
print('------------------------------------------------------------------------\n')
print('Printing the dictionary in the classical Pythonic way:')
print(myDictionary)                                                                     
print('------------------------------------------------------------------------\n')


#---------- ERROR-HANDLING TEST CASES ----------#

# myDictionary.insert("Temple", 12345)                                                  # these lines should return a key error because the key we're trying to insert in the dictionary is not unique
# myDictionary["Temple"] = 12345

# var = myDictionary.get(22)                                                            # these lines should return a key error because the given key is not in the dictionary
# var = myDictionary[22]

# myDictionary.insert([2, 4], 'This is not allowed')                                    # these lines should return a key error because the key we're trying to insert in the dictionary is not an integer, float, or string
# myDictionary[[2, 4]] = 'This is not allowed'

# myDictionary.display(sorted_alphabetically=1)                                         # this line should return a value error because the input argument is not explicitly True or False
