from DoublyLinkedList import DoublyLinkedList
# def remove_duplicates2(self):
#     cur = self.head
#     l1=[]

#     while cur:
      
#         if cur.data in l1:
#             nxt = cur.next
#             self.delete_node(cur.data)
#             cur = nxt
#         else:
#             l1.append(cur.data)
#             cur = cur.next


    
  
# def delete_node(self, node):
#     cur = self.head
#     while cur:
#         if cur == node and cur == self.head:
#             # Case 1:
#             if not cur.next:
#                 cur = None 
#                 self.head = None
#                 return

#             # Case 2:
#             else:
#                 nxt = cur.next
#                 cur.next = None 
#                 nxt.prev = None
#                 cur = None
#                 self.head = nxt
#                 return 

#         elif cur == node:
#             # Case 3:
#             if cur.next:
#                 nxt = cur.next 
#                 prev = cur.prev
#                 prev.next = nxt
#                 nxt.prev = prev
#                 cur.next = None 
#                 cur.prev = None
#                 cur = None
#                 return

#             # Case 4:
#             else:
#                 prev = cur.prev 
#                 prev.next = None 
#                 cur.prev = None 
#                 cur = None 
#                 return 
#         cur = cur.next


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
    # dlist.remove_duplicates2()
    dlist.print_list()
