class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # first add linked list to regular list to use built in reverse
        if self.head:
            current = self.head
            tempList = []
            while(current.get_next() is not None):
                tempList.append(current)
                current = current.get_next()
            tempList.append(current) # need to add tail because above iterator doesn't hit tail
            if len(tempList) > 1:
                # should now be flipped, now I need to iterate the list through and reset all connections
                tempList.reverse()
                # updating connections
                iterator = 0
                for i in tempList:
                    if iterator == 0:
                        self.head = i
                        i.set_next(tempList[1])
                        iterator = iterator + 1
                    elif iterator == len(tempList) - 1:
                        self.tail = i
                        i.set_next(None)
                    else:
                        i.set_next(tempList[iterator + 1])





        
