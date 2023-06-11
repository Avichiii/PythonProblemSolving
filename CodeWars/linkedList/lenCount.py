class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
def length(node: Node):
    head = node
    try:
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count
    except:
        return None
    
def count(node: Node, data: int):
    head = node
    try:
        count = 0
        while head is not None:
            if head.data == data:
                count += 1
            head = head.next
        return count
    except:
        return None
    
node = Node(1, Node(2, Node(3, Node(4, Node(2)))))

print(length(node))
print(count(node, 2))