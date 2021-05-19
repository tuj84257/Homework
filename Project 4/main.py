from data_structures import binarySearchTree, hashTable
from utils import read_songs_from_file, average_node_traversals
from settings import DIRECTORY, FILE_NAME, SIZE_OF_HASH_TABLE

myTree = binarySearchTree()                                                                                                                 # create a binary search tree object
myHashTable = hashTable(SIZE_OF_HASH_TABLE)                                                                                                 # create a hash table object with a given size

read_songs_from_file(DIRECTORY, FILE_NAME, myTree, myHashTable)                                                                             # read and process the data from the file to the respective data structures
average_node_traversals_BST, average_node_traversals_hash_table = average_node_traversals()

print('On average, you need', round(average_node_traversals_BST, 2), 'node traversals to search and find a song in the BST')
print('On average, you need', round(average_node_traversals_hash_table, 2), 'node traversals to search and find a song in the hash table')




# ADDITIONAL FUNCTIONS:

# myTree.print_tree()                                                                                                                       # uncomment the following lines to display the content of the data structures
# print('')
# myHashTable.print_hash_table()

# mySong = myTree.search('Tupac Shakur', 'Don\'t Let Me Down')                                                                              # uncomment the following lines to test the search functionality
# print(mySong.node_traversals_binary_search_tree)
# print(mySong.node_traversals_hash_table)
