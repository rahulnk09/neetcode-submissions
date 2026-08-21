class Node:
    def __init__(self,key:int=0,val:int=0,next: Optional[Node] = None, prev: Optional[Node] = None):
        self.key=key
        self.val=val
        self.next=next
        self.prev=prev
class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}

        self.dh=Node()
        self.dt=Node()
        self.dh.next=self.dt
        self.dt.prev=self.dh
    
    def _remove(self,node):
        nn=node.next
        prev=node.prev

        nn.prev=prev
        prev.next=nn
    
    def _add_to_head(self,node):
        first_node=self.dh.next
        first_node.prev=node
        self.dh.next=node

        node.next=first_node
        node.prev=self.dh

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        cn=self.cache[key]
        self._remove(cn)
        self._add_to_head(cn)
        return cn.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            cn=self.cache[key]
            self._remove(cn)
            self._add_to_head(cn)
            cn.val=value

        else:
            if len(self.cache)>=self.cap:
                tail=self.dt.prev
                self._remove(tail)
                del self.cache[tail.key]


            newnode=Node(key,value)
            self._add_to_head(newnode)
            self.cache[key]=newnode  

        
