'a -> b -> c -> d'

# in preloaded:
class Node:
   def __init__(self, data, next = None):
       self.data = data
       self.next = next


def search_k_from_end(linked_list : Node, k : int):
    list_length = 1
    curr = linked_list
    while curr.next != None:
        curr = curr.next
        list_length += 1
    
    head = linked_list

    kth = list_length
    while kth > 0:
        try:
            if kth == k:
                return head.data
            kth -= 1
            head = head.next
        except:
            return None
        
if __name__ == "__main__":
    list_ = Node(1, Node(2, Node(3, Node(4)))) # 1 -> 2 -> 3 -> 4 -> None
    print(search_k_from_end(list_, 1)) # 4