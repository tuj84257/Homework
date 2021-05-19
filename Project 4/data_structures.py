# This file contains the necessary data structures 
# and methods needed to complete this project

# Class that defines the song object
class song:
    def __init__(self, artist, title):
        self.artist = artist                                                                        # the artist
        self.title = title                                                                          # the song's title
        self.node_traversals_binary_search_tree = 0                                                 # the number of traversals needed to fetch the song object from the binary search tree
        self.node_traversals_hash_table = 0                                                         # the number of traversals needed to fetch the song object from the hash table

# Class that defines a linked list node
class linkedListNode:                               
    def __init__(self, song_object, next=None):
        self.song_object = song_object                                                              # the song object
        self.next = next                                                                            # pointer to the next node in the linked list
  
# Class that defines a binary search tree node        
class binarySearchTreeNode:
    def __init__(self, index, left=None, right=None):
        self.index = index                                                                          # the index returned by the hash function
        self.left = left                                                                            # pointer to the BST node on the left
        self.right = right                                                                          # pointer to the BST node on the left
        self.linkedList = linkedList()                                                              # the linked list to handle collisions
        
# Class that defines a linked list        
class linkedList:
    def __init__(self):
        self.head = None                                                                            # the head of the linked list (points to None by default)
    
    # method that prints the linked list
    # (can be used to check the content of 
    # the linked list for testing purposes)
    def printList(self):
        currNode = self.head                                                                        # start by pointing to the head of the linked list
        while currNode is not None:                                                                 # as long as the end of the linked list has not been reached
            if currNode.next is None:                                                               
                print(currNode.song_object.artist, currNode.song_object.title, end="")              #   print the artist and the title of the song object stored in the current node
            else:
                print(currNode.song_object.artist, currNode.song_object.title, end=" -> ")
            currNode = currNode.next                                                                #   move to the next node
        print('')
    
    # method that appends a node containing
    # a song object to the linked list
    def add(self, song_object):                                                     
        newNode = linkedListNode(song_object, None)                                                 # encapsulate the song object in a linked list node
        tail = self.head                                                                            # start from the head of the linked list
        if self.head == None:                                                                       # if head points to None, that means the list is empty                                             
            self.head = newNode                                                                     #   therefore, make head point to the new node
        else:                                                                                       # else                            
            while tail.next != None:                                                                #   traverse to the tail of the linked list
                tail = tail.next
            tail.next = newNode                                                                     #   and append the new node
    
    # method that finds a song object in the
    # linked list, given its artist and title
    def find_song(self, artist, title):
        n = 0                                                                                       # use this variable to record the number of linked list node traversals
        currNode = self.head                                                                        # start from the head of the linked list
        n += 1                                                                                      # increment the number of node traversals
        while currNode is not None:                                                                 # as long as the end of the linked list has not been reached                                                       
            if currNode.song_object.artist == artist and currNode.song_object.title == title:       #   if the current node contains a song object that matches the given information
                return [currNode.song_object, n]                                                    #     return a list with the song object and the number of nodes that were traversed during the search operation
            currNode = currNode.next                                                                #   move to the next node
            n += 1                                                                                  # increment the number of node traversals

# Class that defines a binary search tree
class binarySearchTree:
    def __init__(self):
        self.root = None                                                                            # the root of the binary search tree (points to None by default)
    
    # method that inserts a node into
    # the binary search tree
    def insert(self, index, song_object):
        newNode = binarySearchTreeNode(index)                                                       # create a new binary search tree node, containing the given index, and a linked list object to handle collisions
        if self.root is None:                                                                       # if the tree is empty
            self.root = newNode                                                                     #   make the new node the root of the tree
            self.root.linkedList.add(song_object)                                                   #   add the song object to its linked list
            # print('inserted', newNode.index, 'as root')                                           #   you can uncomment this for debugging purposes
            return                                                                                  #   return
        currNode = self.root                                                                        # start from the root of the binary search tree
        while currNode is not None:                                                                 # as long as you're inside the tree
            if index == currNode.index:                                                             #   if the index of the current node matches the given index (which means that there is a collision)
                currNode.linkedList.add(song_object)                                                #     add the song object to its linked list
                return                                                                              #     return
            prevNode = currNode                                                                     #   keep track of the previous node
            currNode = currNode.left if index < currNode.index else currNode.right                  #   move left if the given index is smaller than the index of the current node; else, move right
        if index < prevNode.index:                                                                  # now that you have arrived to the desired location, if the given index is smaller than the index of the previous node (which is a leaf)
            prevNode.left = newNode                                                                 #   insert the new node to the left of the previous node
            prevNode.left.linkedList.add(song_object)                                               #   add the song object to the node's linked list
            # print('inserted', newNode.index, 'left of', prevNode.index)                           #   you can uncomment this for debugging purposes
        else:                                                                                       # else
            prevNode.right = newNode                                                                #   insert the new node to the right of the previous node
            prevNode.right.linkedList.add(song_object)                                              #   add the song object to its linked list
            # print('inserted', newNode.index, 'right of', prevNode.index)                          #   you can uncomment this for debugging purposes
    
    # utility method to print the tree recursively
    # (can be used to check the content of 
    # the tree for testing purposes)
    def print_recursively(self, rootNode):
        if rootNode is None:                                                                        # this method prints the binary search tree in a pre-order manner
            return
        print(rootNode.index, ':', end=" ")
        rootNode.linkedList.printList()
        self.print_recursively(rootNode.left)
        self.print_recursively(rootNode.right)
    
    # method that prints the tree recursively
    # starting from its root
    def print_tree(self):
        print('Printing the tree...')
        print('-----------------------')
        self.print_recursively(self.root)
    
    # method that finds and returns a song object
    # in the tree, given its artist and title
    def search(self, artist, title):
        from utils import hash_function                                                             # import the hash function
        index = hash_function(artist, title)                                                        # calculate the index based on the given song information
        n = 0                                                                                       # use this variable to record the number of binary search tree node traversals
        currNode = self.root                                                                        # start from the root of the tree
        n += 1                                                                                      # increment the number of node traversals
        while currNode.index != index:                                                              # as long as you have not arrived at the calculated index
            if index < currNode.index:                                                              #   if the given index is smaller than the index of the current node
                currNode = currNode.left                                                            #     move to the node on the left
            else:                                                                                   #   else
                currNode = currNode.right                                                           #     move to the node on the right
            n += 1                                                                                  #   increment the number of node traversals
        the_song, number_of_linked_list_traversals = currNode.linkedList.find_song(artist, title)   # fetch the found song object, and number of nodes that were traversed during the search operation in the linked list
        the_song.node_traversals_binary_search_tree = number_of_linked_list_traversals + n          # store the total number of binary search tree traversals in the song object
        return the_song                                                                             # return the found song object

# Class that defines a hash table
class hashTable:
    def __init__(self, size):
        self.buffer = []                                                                            # the hash table array (initialize it as an empty list)
        self.size = size                                                                            # the size of the hash table
        for i in range(size):
            self.buffer.append(linkedList())                                                        # fill the array cells with linked list objects
    
    # method that inserts a node to the hash table        
    def insert(self, bufferIndex, song_object):
        self.buffer[bufferIndex].add(song_object)                                                   # add the song object to the linked list located in the given hash table index
    
    # utility method to print the hash table
    # (can be used to check the content of 
    # the hash table for testing purposes)    
    def print_hash_table(self):
        print('Printing the hash table...')
        print('-----------------------')
        for i in range(self.size):                                  
            print(i, ':', end=" ")                                                                  # display the array index (on the left)                                        
            self.buffer[i].printList()                                                              # display the songs stored in the linked list (on the right)
     
    # method that finds and returns a song object
    # in the hash table, given its artist and title            
    def search(self, artist, title):
        from utils import hash_function                                                             # import the hash function
        bufferIndex = hash_function(artist, title)                                                  # calculate the index based on the given song information
        n = 0                                                                                       # use this variable to record the number of hash table node traversals
        bufferLocation = self.buffer[bufferIndex]                                                   # go to the memory location with the calculated index
        n += 1                                                                                      # increment the number of node traversals
        the_song, number_of_linked_list_traversals = bufferLocation.find_song(artist, title)        # fetch the found song object, and number of nodes that were traversed during the search operation in the linked list
        the_song.node_traversals_hash_table = number_of_linked_list_traversals + n                  # store the total number of hash table traversals in the song object
        return the_song                                                                             # return the found song object
        