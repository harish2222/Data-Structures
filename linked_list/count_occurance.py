from LinkedList import LinkedList

if __name__  == '__main__':
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(2)
    llist.append(6)
    llist.append(6)
    llist.append(6)
    b = llist.count_occurences_iterative(6)
    c = llist.count_occurences_recursive(llist.head.next,2)
    print(b)
    print(c)
    
    
    
    