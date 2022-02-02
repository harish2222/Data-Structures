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

    def merge_sorted(self, llist):

        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                # Remove node:
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    def print_nth_node_from_last_sol1(self, n):
        total_len = self.len_iterative()

        cur = self.head
        while cur:
            if total_len == n:
                print(cur.data)
                return cur.data
            total_len -= 1
            cur = cur.next
        if cur is None:
            return

    def print_nth_node_from_last_sol2(self, n):
        x = self.head
        y = self.head

        if n > 0:
            count = 0
            while y:
                count += 1
                if(count >= n):
                    break
                y = y.next

            if not y:
                print(str(n) + " is greater than the number of nodes in list.")
                return

            while x and y.next:
                x = x.next
                y = y.next

            return x.data
        else:
            return None

    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    def is_palindrome(self):
        if self.head:
            p = self.head
            q = self.head
            prev = []

            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]

            count = 1

            while count <= i//2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True


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

    print('Print from Nth to Last node')
    llist.print_nth_node_from_last_sol1(4)
    llist.print_nth_node_from_last_sol1(3)

    print('Print from Nth to Last node')
    # print(llist.print_nth_node_from_last_sol2(1))
    print(llist.print_nth_node_from_last_sol2(3))
