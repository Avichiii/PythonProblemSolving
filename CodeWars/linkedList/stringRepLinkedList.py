class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def stringify(node : Node):
    if node == None:
        return None
    
    curr =  node
    returnString = ''
    while True:
        returnString += f'{curr.data} -> '
        if curr.next == None:
            break
        curr = curr.next 
    return returnString + 'None'


if __name__ == "__main__":
    list_ = Node(1, Node(2, Node(3, Node(4)))) # 1 -> 2 -> 3 -> 4 -> None
    print(stringify(list_)) # '1 -> 2 -> 3 -> 4 -> None'