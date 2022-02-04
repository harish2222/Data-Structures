from CircularLinkedList import CircularLinkedList

if __name__ == '__main__':
    clist1 = CircularLinkedList()
    clist1.append(1)
    clist1.append(2)
    clist1.append(3)
    clist1.append(4)
    clist1.append(5)
    clist1.append(6)

    #clist1.josephus_circle(step = 3)
    clist1.josephus_circle(step = 2)
    
    #clist1.josephus_circle(step = 1)
    clist1.print_list()
