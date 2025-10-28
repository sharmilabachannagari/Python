class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(0)  # A dummy node to simplify code
        current = dummy_head  # Pointer to build the new linked list
        carry = 0  # Initialize carry as 0

        while l1 or l2 or carry:
            # Get the current digits (if the list is short, treat them as 0)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Sum the digits and the carry
            total = val1 + val2 + carry

            # Update carry for the next iteration
            carry = total // 10

            # Create the next node in the result linked list
            current.next = ListNode(total % 10)

            # Move to the next node
            current = current.next

            # Move to the next nodes in the input linked lists, if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next  # Return the next node after the dummy head
