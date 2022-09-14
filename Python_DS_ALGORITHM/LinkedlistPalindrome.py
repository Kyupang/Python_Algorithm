
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)
def print_my(Node):
    node= head
    while node.next:
        print(node.data,end = "->")
        node =node.next
    print(node.data)


class solution:
    def isPalindrome(self,head: Node) ->bool:
        q: list = []

        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.data)
            node = node.next

        while len(q) >1:
            if q.pop(0) != q.pop():
                return False
        return True
node1 = Node(1)
head = node1
add(2)
add(2)
add(1)

print_my(node1)

sol = solution()
print(sol.isPalindrome(node1))

