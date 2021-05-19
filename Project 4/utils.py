# This file contains utility functions needed to calculate 
# the output of the hash function, read the data from the
# songs list file to the respective data structures, and 
# calculate the average number of node traversals needed
# to find a song object in these data structures

from data_structures import song
from settings import SIZE_OF_HASH_TABLE
import os

global node_traversals_BST, node_traversals_hash_table
node_traversals_BST = []                                                                            # these lists will consist of the number of node traversals needed to arrive at 
node_traversals_hash_table = []                                                                     # each song in the file for each respective data structure

# The hash function
def hash_function(artist, title):
    sum_of_ordinal_values = 0
    song_string = artist + title
    for character in song_string:
        sum_of_ordinal_values = sum_of_ordinal_values + (ord(character))**2
    return sum_of_ordinal_values % SIZE_OF_HASH_TABLE

# function that reads all songs from the file, inserts them into
# the respective data structures, and searches them to find the
# number of node traversals needed to arrive at each song object
def read_songs_from_file(directory, file_name, binary_search_tree, hash_table):
    os.chdir(directory)
    with open(file_name, 'r') as song_file:                                                         # open the file
        for line in song_file:                                                                      # for each line in the file
            artist, title = line.split(", ")                                                        #   fetch the song artist and title
            index = hash_function(artist, title[:-1])                                               #   calculate the memory location index where the song object will be stored in each data structure
            song_object = song(artist, title[:-1])                                                  #   create a new song object (ignoring the newline character in the title)
            binary_search_tree.insert(index, song_object)                                           #   insert the song object in the binary tree
            found_song = binary_search_tree.search(artist, title[:-1])                              #   search for the song in the binary tree, and fetch it from the data structure
            node_traversals_BST.append(found_song.node_traversals_binary_search_tree)               #   append the number of node traversals needed to find the song in the tree to the node_traversals_BST array
            hash_table.insert(index, song_object)                                                   #   insert the song object in the hash table
            found_song = hash_table.search(artist, title[:-1])                                      #   search for the song in the hash table, and fetch it from the data structure
            node_traversals_hash_table.append(found_song.node_traversals_hash_table)                #   append the number of node traversals needed to find the song in the hash table to the node_traversals_hash_table array
    return

# function that returns a list of the average number of node traversals 
# needed to find a song object in the binary search tree and hash table
def average_node_traversals():
    return [                                                                            
            sum(node_traversals_BST)/len(node_traversals_BST), 
            sum(node_traversals_hash_table)/len(node_traversals_hash_table)
    ]  
