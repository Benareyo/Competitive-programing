class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # Dummy node to serve as the start of the result list
        current = dummy  # Pointer to build the new list
        carry = 0  # Initialize carry to 0
        
        while l1 or l2 or carry:
            # Get values from the nodes, default to 0 if nodes are None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Compute the sum of the two digits and carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry for the next digit
            new_digit = total % 10  # Compute the new digit to add to the list
            
            # Create a new node with the computed digit
            current.next = ListNode(new_digit)
            current = current.next  # Move to the next node
            
            # Move to the next nodes in the input lists, if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next  # Return the next node to skip the dummy node

# Helper function to print the linked list
def printLinkedList(head: ListNode):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next
