from DoublyLinkedList import DoublyLinkedList

if __name__ == '__main__':
    dlist = DoublyLinkedList()
    dlist.append(1)
    dlist.append(2)
    dlist.append(3)
    dlist.append(143)
    dlist.append(6)
    dlist.append(16)
    
    dlist.add_after_node(143,43)
    dlist.add_before_node(143,23)
    dlist.print_list()