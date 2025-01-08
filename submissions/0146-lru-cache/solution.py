class LRUCache:
    # We create a class that uses orderedDict to track first and last items
    # When an item is used we move it to the back.
    # When cache is full we pop the LeastRecentlyUsed
    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.key_list = OrderedDict()

    def get(self, key: int) -> int:        
        if key not in self.key_list:
                    return -1
        # If key exists, update the value and mark as recently used
        self.key_list.move_to_end(key)
        return self.key_list[key]

    def put(self, key: int, value: int) -> None:
        if key in self.key_list:
            self.key_list.move_to_end(key)
        self.key_list[key] = value
        if len(self.key_list) > self.max_capacity:
        # Pop the least recently used (first) item
            self.key_list.popitem(last=False)

