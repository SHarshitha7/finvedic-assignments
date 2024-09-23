class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:  
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)

        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        curr_node.next = new_node

    def sortedMerge(self, a, b):
        result = None

        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result

    def mergeSort(self, h):
        if h is None or h.next is None:
            return h

        middle = self.getMiddle(h)
        nexttomiddle = middle.next

        middle.next = None

        left = self.mergeSort(h)
        right = self.mergeSort(nexttomiddle)

        sortedlist = self.sortedMerge(left, right)
        return sortedlist

    def getMiddle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

def printlist(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        if curr_node.next is None:
            print(curr_node.data, end="")
        else:
            print(curr_node.data, end=" -> ")
        curr_node = curr_node.next
    print('')

if __name__ == '__main__':
    li = LinkedList()

    n = int(input("Enter number of elements to insert: "))
    print("Enter the elements:")

    for _ in range(n):
        value = int(input())
        li.append(value)

    print("Linked list before sorting:")
    printlist(li.head)

    li.head = li.mergeSort(li.head)

    print("Linked list after sorting:")
    printlist(li.head)
