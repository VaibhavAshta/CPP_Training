# Linked list implementation in Python
class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

linked_list = LinkedList

def connectingnode(linked_list,second,third,fourth):
    # Connect nodes
    linked_list.head.next = second
    second.next = third
    third.next = fourth

def displayingnode():
    while linked_list.head != None:
            print(linked_list.head.item, end=" ")
            linked_list.head = linked_list.head.next
    print("\n")

user = input("Where would you like to add a node\n1)In the beginning\n2)In the middle\n3)In the end\n4)Deleting a node\n: ")
if user == "1":
    firstnode = input("Please enter the value of the node : ")
    linked_list.head = Node(firstnode)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    connectingnode(linked_list,second,third,fourth)
    displayingnode()

elif user == "2":
    ask = input("Where would you like to add, after which node (first or second): ")
    if ask == "first" or ask == "1":
        firstnode = Node(1)
        linked_list.head = firstnode
        middlenode = input("Please enter the middle node value : ")
        second = Node(middlenode)
        third = Node(3)
        fourth = Node(4)

        connectingnode(linked_list,second,third,fourth)
        displayingnode()
    
    elif ask == "second" or ask == "2":
        firstnode = Node(1)
        linked_list.head = firstnode
        middlenode = input("Please enter the middle node value : ")
        second = Node(2)
        third = Node(middlenode)
        fourth = Node(4)
        
        connectingnode(linked_list,second,third,fourth)
        displayingnode()
    
elif user == "3":
    lastnode = input("Please enter the last node value : ")
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(lastnode)
    connectingnode(linked_list,second,third,fourth)
    displayingnode()

elif user == "4":
    firstnode = Node(1)
    linked_list.head = firstnode
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    connectingnode(linked_list,second,third,fourth)
    print("The values : ")
    displayingnode()
    ask = input("which node with the above value would you like to delete (1,2,3,4): ")
    if ask == "1":
        second = Node(2)
        linked_list.head = second
        third = Node(3)
        fourth = Node(4)
        second = third
        third = fourth
        connectingnode(linked_list,second,third,None)
        displayingnode()
    
    elif ask == "2":
        first = Node(1)
        linked_list.head = first
        third = Node(3)
        fourth = Node(4)
        second = third
        third = fourth
        connectingnode(linked_list,second,third,None)
        displayingnode()
            
    elif ask == "3":
        first = Node(1)
        linked_list.head = first
        fourth = Node(4)
        second = Node(2)
        third = fourth
        connectingnode(linked_list,second,third,None)
        displayingnode()
    
    elif ask == "4":
        first = Node(1)
        linked_list.head = first
        second == Node(2)
        third = Node(3)

        connectingnode(linked_list,second,third,None)
        displayingnode()