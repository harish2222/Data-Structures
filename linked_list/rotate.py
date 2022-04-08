from LinkedList import LinkedList
if __name__ == '__main__':
    llist = LinkedList()
    llist.append(1)
    llist.append(3)
    llist.append(2)
    llist.append(5)
    llist.append(4)
    print('Original Linked List')
    
    llist.print_list()
    
    print('\nRotated Linked List')
    
    llist.rotate(2)
    llist.print_list()