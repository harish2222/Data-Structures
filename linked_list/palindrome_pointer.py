from LinkedList import LinkedList

if __name__ == '__main__':
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(4)
    llist.append(4)
    llist.append(2)
    llist.append(1)
    
    llist.print_list()

    print(llist.is_palindrome())


