from FingerTable import FingerTable

class Node:
    def __init__(self, node_id):
        self.id = node_id
        self.successor = None
        self.predecessor = None
        self.finger_table = FingerTable(self)
        self.local_keys = {}

    def join(self, node):
        if node is None:
            # First node joining the Chord network
            self.predecessor=self
            self.successor=self
            for i in range(1, 8 + 1):
                self.finger_table.set(i, self.successor.id)
            self.finger_table.pretty_print()
        else:
            print(f"Node {self.id} joining the Chord network.")
            # Finding the Position of the Node to Join the FingerTable
            while node.successor.id<self.id:
                node = node.successor
                if node.successor.id<=node.id:
                    break
            # Assigning the predecessor and Successor Nodes, updating Finger Table and Migrating the Nodes
            self.successor = node.successor
            self.predecessor = node
            node.successor = self
            self.successor.predecessor = self
            self.update_finger_table(self)
            self.update_finger_table(self.successor)
            self.update_finger_table(self.predecessor)
            self.migrate_keys(self.successor)
            self.finger_table.pretty_print()

    def update_finger_table(self, node):
        for i in range(1, 8 + 1):
            key = self.id + 2**(i-1) % 256
            successor = self.find_successor(key, node, [])
            self.finger_table.set(i, successor.id)

    def migrate_keys(self, successor):
        lst = []
        for key, value in successor.local_keys.items():
            if successor is not None and key<=self.id:
                self.local_keys[key]=value
                print(f"Migrate key {key} from node {successor.id} to node {self.id}")
                lst.append(key)
        for val in lst:
            del successor.local_keys[val]

    def insert(self, key, *args):
        node_insert = self.find_key_node(key, self)
        print(f"Inserting key {key} in node {node_insert.id}")
        if args:
            node_insert.local_keys[key] = args[0]
        else:
            node_insert.local_keys[key] = None
        print(f"---------------Node id:{node_insert.id}---------------")
        print(node_insert.local_keys)

    def find_key_node(self, key, node):
        if key==node.id:
            return node
        if key>node.id and node.successor.id<node.id:
            return node.successor
        if key>node.id and key<node.successor.id:
            return node.successor
        else:
            return self.find_key_node(key, node.successor)

    def lookup(self):
        self.lookupall(self, 0)

    def lookupall(self, origNode, count):
        if origNode == self and count>0:
            return
        if not count:
            print("----------Node id: {}----------".format(str(self.id)))
        path = [origNode.id]
        if origNode != self:
            path.append(self.id)
        for key, value in self.local_keys.items():
            print("Lookup result of key {key} from node {node_id} with path {path} value is {value}".format(
                key = str(key), 
                node_id = str(origNode.id),
                path = str(path),
                value = str(value)
            ))
        self.successor.lookupall(origNode, count+1)

    def find_successor(self, key, node, visitednodes):
        lst = visitednodes
        if node.id==key:
            return node
        if key>node.id:
            if node.id in lst:
                return node.successor
            else:
                lst.append(node.id)
                if node.successor.id>node.id:
                    return self.find_successor(key, node.successor, lst)
                else:
                    return node.successor
        if key<node.id and key>node.predecessor.id:
            return node
        if key<node.id:
            lst.append(node.id)
            return self.find_successor(key, node.successor, lst)

    def remove(self, key):
        node_remove = self.find_key_node(key, self)
        if key in node_remove.local_keys:
            print(f"Removed key {key} in node {node_remove.id}")
            del node_remove.local_keys[key]
        else:
            print("Key not found in any Node")


    def PrettyPrintKeys(self):
        while self.successor.id>self.id:
            self = self.successor
        self=self.successor
        while self.successor.id>self.id:
            print(f"---------------Node id:{self.id}---------------")
            print(self.local_keys)
            self = self.successor
        print(f"---------------Node id:{self.id}---------------")
        print(self.local_keys)
        self = self.successor

    def find(self, key):
        dest_node = self.find_node_of_key(key, True) 
        if key not in dest_node.local_keys.keys():
            print("Key {} not found\n".format(key))
        else:
            val = dest_node.local_keys.get(key)
            print("Key is Found! The value for key {0} is {1}\n".format(key, val))
        

    def find_node_of_key(self, key, key_flag=False):
        node = self.check_key_in_node(key, key_flag)
        if node:
            return node
        
        if key < self.id:
            difference = 256 - self.id + key
        else:
            difference = key - self.id
        two_power_count = -1
        while difference:
            difference = difference//2
            two_power_count += 1
        for _ in range(two_power_count):
            search_node = self.successor
        search_node = search_node.successor

        node = search_node.check_key_in_node(key, key_flag)
        if node:
            return node
        
        if search_node.predecessor.id > key and search_node.predecessor == self:
            return search_node.predecessor
        else:
            return search_node.find_node_of_key(key, key_flag)

    def check_key_in_node(self, key, key_flag):
        if key == self.id:
            return self
        if (self.predecessor == self == self.successor):
            if key_flag:
                return self.predecessor
            return self
        if (self.predecessor.id < key < self.id):
            return self
        if (self.predecessor.id > self.id):
            if (key > self.predecessor.id):
                return self
            if (key < self.predecessor.id and key < self.id):
                return self
        if (self.predecessor.id > self.id and key < self.id and key > self.predecessor.id):
            return self

    # OPTIONAL IMPLEMENTATION
    def leave(self):
        print(f"Node {self.id} leaving the Chord network.")
        # TODO: Implement finger table update based on leave