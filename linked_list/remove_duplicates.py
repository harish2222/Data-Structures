from LinkedList import LinkedList

if __name__ == '__main__':
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(3)
    llist.append(2)
    llist.remove_duplicates()
    llist.print_list()