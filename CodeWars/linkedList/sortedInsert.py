class Node:
   def __init__(self, data, next = None):
       self.data = data
       self.next = next

def sorted_insert(head: Node, data):
    new_node = Node(data)
    if head is None or data < head.data:
        new_node.next = head
        return new_node

    current = head
    while current.next is not None and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node
    return head

if __name__ == "__main__":
    list_ = Node(1, Node(2, Node(4, Node(5)))) # 1 -> 2 -> 4 -> 5 -> None
    print(sorted_insert(list_, 3)) 