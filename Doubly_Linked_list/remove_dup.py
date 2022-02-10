from DoublyLinkedList import DoublyLinkedList


if __name__ == '__main__':
    dlist = DoublyLinkedList()
    dlist.append(11)
    dlist.append(2)
    dlist.append(12)
    dlist.append(33)
    dlist.append(2)
    dlist.append(12)
    dlist.append(3)
    dlist.append(2)
    dlist.append(12)


    dlist.print_list()
    dlist.remove_duplicates()
    #dlist.remove_duplicates1()
    dlist.print_list()
