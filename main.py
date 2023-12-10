import sys
from Node import Node

map_node_name = {}

# Read the testcase.txt File
with open(sys.argv[-1], 'r') as f:
    input_file = f.read()

testcases = input_file.split('\n')

for testcase in testcases:
    
    command = testcase.split(" ")[0]
    params = testcase.split(" ")[1:]

    # Add a New Node 
    if command=="newnode":
        map_node_name[params[0]] = Node(int(params[1]))

    # Joins a Node to the Chord Network
    if command == "join":
        if params[1] != 'None':
            newNode = map_node_name[params[0]]
            existingNode = map_node_name[params[1]]
            newNode.join(existingNode)
        else:
            newNode = map_node_name[params[0]]
            newNode.join(None)

    # Prints FingerTable of a Node
    if command == "prettyprintFinger":
        node = map_node_name[params[0]]
        node.finger_table.pretty_print()

    # Insert key:value into the Finger Table
    if command == "insert":
        node = map_node_name[params[0]]
        if len(params)==3:
            node.insert(int(params[1]), int(params[2]))
        else:
            node.insert(int(params[1]))

    # Returns the Lookup of all Keys in a specific Node
    if command == "lookupall":
        node = map_node_name[params[0]]
        node.lookup()

    # Finds key from a Node
    if command == "find":
        node = map_node_name[params[0]]
        node.find(int(params[1]))

    # Removes key from a Node 
    if command == "remove":
        node = map_node_name[params[0]]
        node.remove(int(params[1]))

    # Prints all the Keys in Nodes
    if command == "prettyprintKeys":
        node = map_node_name[params[0]]
        node.PrettyPrintKeys()


exit()

