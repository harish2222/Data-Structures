from LinkedList import LinkedList,Node
  
if __name__ == '__main__':
    llist_1 = LinkedList()
    llist_2 = LinkedList()

    llist_1.append(1)
    llist_1.append(5)
    llist_1.append(7)
    llist_1.append(9)
    llist_1.append(10)

    llist_2.append(2)
    llist_2.append(3)
    llist_2.append(4)
    llist_2.append(6)
    llist_2.append(8)

    llist_1.merge_sorted(llist_2)
    llist_1.print_list()