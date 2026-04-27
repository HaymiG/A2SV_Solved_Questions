# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head: #if the list is empty
            return head 
        a=b=head #making two pointers
        for i in range(n): # getting b n pointers ahead
            b=b.next
        if not b: #if b reached the end of list that means n is first element to be deleted
            return head.next #to delete we just skip the head and start from +1
        while b.next: #stop the traversal at last elemen, so our a is 1 before to be deleted
            a=a.next #traversing both pointers
            b=b.next
        a.next=a.next.next #a's next is to be deleted just skip it, make it it's next one
        return head #return  the list

        
        