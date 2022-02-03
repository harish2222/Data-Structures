from LinkedList import LinkedList

if __name__ == '__main__':

    llist1 = LinkedList()
    llist1.append(4)
    llist1.append(2)
    llist1.append(1)
    llist2 = LinkedList()
    llist2.append(4)
    llist2.append(1)
    llist2.append(3)
    
    # 124 + 314 = 438
    x = llist1.sum_two_lists(llist2)
    print(x)