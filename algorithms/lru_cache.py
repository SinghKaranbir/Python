import doubly_linked_list as dll

class LRUCache:
    '''
    LRUCache represents cache with LRU Heuristic
    '''

    capacity = 0
    doubly_list = dll.DoublyLinkedList()
    node_map = {}

    def __init__(self, capacity):
        '''
        Initliaze the cache with fixed capacity
        '''
        self.capacity = capacity

    def get(self, key):
        '''
        Get the value of the key if present else -1
        '''
        if key in self.node_map:
            node = self.node_map[key]
            # Delete the Node to move it to front of the list
            self.doubly_list.delete(node)
            # Add it back again
            self.doubly_list.insert(node)
            return node.pair[1]

        return -1


    def put(self, key, value):
        '''
        Put the key, value pair in the cache, if cache is full, delete the least
        recently used value
        '''
        if key in self.node_map:
            node = self.node_map[key]
            # Delete the Node to move it to front of the list
            self.doubly_list.delete(node)
            # Update the value of the node
            node.pair = (key, value)
            # Add it back to the Doubly Linked List
            self.doubly_list.insert(node)
            self.node_map[key] = node
        else:
            # LRU has reached the capacity, so we need to delete the least recently used value
            if len(self.node_map) == self.capacity:
                deleted = self.doubly_list.delete_last()
                self.node_map.pop(deleted.pair[0])

            # Add the new value
            node = dll.Node((key, value))
            self.node_map[key] = node
            self.doubly_list.insert(node)

    def __repr__(self):
        return repr(self.doubly_list)


if __name__ == '__main__':
    cache = LRUCache(3)
    cache.put(1, 2)
    cache.put(2, 3)
    cache.put(3, 5)
    assert cache.get(1) == 2

    cache.put(4, 7)
    assert repr(cache) == '[4,7]->[1,2]->[3,5]->'

    print('Current Cache: {}'.format(repr(cache)))
