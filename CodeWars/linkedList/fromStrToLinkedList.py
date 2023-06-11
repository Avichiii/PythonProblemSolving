class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(str_node: str):
    str_node = str_node.split(' -> ')

    link_node = Node(int(str_node[0]))
    curr = link_node
    
    for str_data in str_node[1:]:
        if str_data == 'None':
            continue

        new_node = Node(int(str_data))
        curr.next = new_node
        curr = new_node

    return link_node

if __name__ == "__main__":
    linkedList = linked_list_from_string('1 -> 2 -> 3 -> 4 -> None') # 1 -> 2 -> 3 -> 4 -> None
    curr = linkedList
    data = ''
    while curr.next != None:
        data += f'{curr.data} -> '
        curr = curr.next
    print(data + 'None')
    '''
    1 ->  2 -> None
    '''