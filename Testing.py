class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while (start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        cur_node = head
        prev_node = None
        dic_check = {}
        while cur_node:
            if cur_node.data in dic_check:
                prev_node.next = cur_node.next
                cur_node = None
                cur_node = prev_node.next
            else:
                dic_check[cur_node.data] = True
                prev_node = cur_node
                cur_node = cur_node.next

        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
