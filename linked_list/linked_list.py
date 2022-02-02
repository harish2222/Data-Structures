from re import A


class Node:

    def __init__(self, data):

        self.data = data

        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    def append(self, data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node

            return

        last_node = self.head

        while last_node.next:

            last_node = last_node.next

        last_node.next = new_node

    def print_list(self):

        cur_node = self.head

        while cur_node:

            print(cur_node.data, "->", end=" ")

            cur_node = cur_node.next

    def insert_after_node(self, prev_node, data):

        if not prev_node:

            print("Previous node does not exist.")

            return

        new_node = Node(data)

        new_node.next = prev_node.next

        prev_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None

            return

        prev = None

        while cur_node and cur_node.data != key:

            prev = cur_node

            cur_node = cur_node.next

        if cur_node is None:

            return

        prev.next = cur_node.next

        cur_node = None

    def delete_node_at_pos(self, pos):

        if self.head:

            cur_node = self.head

            if pos == 0:

                self.head = cur_node.next

                cur_node = None

                return

        prev = None

        count = 0

        while cur_node and count != pos:

            prev = cur_node

            cur_node = cur_node.next

            count += 1

        if cur_node is None:

            return

        prev.next = cur_node.next

        cur_node = None

    def len_iterative(self):

        count = 0

        cur_node = self.head

        while cur_node:

            count += 1

            cur_node = cur_node.next

        return count

    def len_recursive(self, node):

        if node is None:

            return 0

        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
    
        prev = None 
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
        
        self.head = prev
        
    def reverse_recursive(self):
    
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)
        
        
        
if __name__ == "__main__":
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.append("E")
    llist.append("F")
    llist.append("G")
    llist.append("T")

    llist.prepend("H")
    llist.insert_after_node(llist.head.next.next.next, "S")
    llist.delete_node("A")
    llist.delete_node_at_pos(3)
    print(llist.len_iterative())
    print(llist.len_recursive(llist.head.next))
    llist.print_list()
    print("\n")
    # print(llist.head)
    print('Swap of H and C')
    llist.swap_nodes('H', 'C')
    print("\n")

    print('Swap of B and E')
    llist.swap_nodes('B', 'E')
    print("\n")
    
    llist.swap_nodes('V', 'E')
    llist.print_list()
    print("\n")

    # Iterative reversing 
    print('Reverse Iterative')
    llist.reverse_iterative()
    llist.print_list()
    print("\n")

    print('Reversive Recursive')
    llist.reverse_recursive()
    llist.print_list()
    print("\n")