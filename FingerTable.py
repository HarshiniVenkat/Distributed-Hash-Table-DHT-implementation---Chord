class FingerTable:
    def __init__(self, node):
        self.node = node
        self.finger_table = {}  # Index starts from 1

    def set(self, index, successor):
        self.finger_table[index] = successor

    def get(self, index):
        return self.finger_table[index]

    def pretty_print(self):
        print(f"--------------Node id:{self.node.id}----------------")
        print(f"Successor:{self.node.successor.id}  Predecessor:{self.node.predecessor.id}")
        print("FingerTables:")
        for k in range(1,9):
            resolve = (self.node.id + 2**(k-1))%256
            # print("Resolved is:", resolve)
            print(f"| k = {k} [{str((self.node.id + 2**(k-1)) % 256)} , {str((self.node.id + 2**k) % 256)})    succ. = {(self.node.find_successor(resolve, self.node, [])).id} | ")
        print("-------------------------------------------")
        print("*******************************************")