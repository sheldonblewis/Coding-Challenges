# *** SUB-20 MINUTES ***


# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Example:

# Input: lists = [[1->4->5],[1->3->4],[2->6]]
# Output: [1->1->2->3->4->4->5->6]

# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.val))
            current = current.next
        return ' -> '.join(result)

def mergeLists(lists):
    heap = []

    for list in lists:
        if list.head:
            heapq.heappush(heap, (list.head.val, id(list.head), list.head))
    
    temp = ListNode(0)
    current = temp
    
    while heap:
        val, _, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.val, id(node.next), node.next))
    
    return temp.next

if __name__ == "__main__":
    lists = []
    print("Enter Linked Lists as rows of numbers separated by spaces, and press enter to input a new Linked List (enter an empty line to stop.\n\nExample:\n1 4 5\n1 3 4\n2 6\n\nYour Turn:\n")
    while True:
        try:
            line = input()
            if not line.strip():
                break
            numbers = list(map(int, line.split()))
            linked_list = LinkedList()
            for number in numbers:
                linked_list.append(number)
            lists.append(linked_list)
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
    
    merged = mergeLists(lists)
    
    while merged:
        print(merged.val)
        merged = merged.next
