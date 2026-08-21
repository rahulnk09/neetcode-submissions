class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node

        # Dummy boundary nodes to simplify edge cases
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper: remove a node from the linked list
    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Helper: insert a node right after head (Most Recently Used)
    def _add_to_head(self, node: Node) -> None:
        first_node = self.head.next
        node.prev = self.head
        node.next = first_node
        self.head.next = node
        first_node.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Move node to head because it was recently accessed
        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move to head
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Evict LRU node if capacity is reached
            if len(self.cache) >= self.cap:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]

            # Add new node to head and dictionary
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)