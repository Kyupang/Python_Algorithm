class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class solution:
    def isPalindrome(self,head: ListNode) -> bool:
        q: list = []

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True


sol = solution()
linkedlist1 = ListNode(1)
linkedlist2 = ListNode(2)
linkedlist3 = ListNode(2)
linkedlist4 = ListNode(1)

linkedlist1.next = linkedlist2
linkedlist2.next = linkedlist3
linkedlist3.next = linkedlist4

print(sol.isPalindrome(linkedlist1))