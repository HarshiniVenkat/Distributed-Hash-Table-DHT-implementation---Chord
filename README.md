# Chord_DHT_Implementation
A Python Implementation of the Chord Protocol in Computer Networds


### **Running the code:**
-  ```python3 main.py <test input file>```
 <br>(Ex: ```python3 main.py testcase.txt```)

### **Testcase file:**
- The testcase file will contain a list of commands with a command in each line.
- Each command has the commandName, followed by parameters that the command takes
- An example testcase file is included with the project ```testcase.txt```.
- Here are the commands implemented and their format with examples below:
    - *Creating/Adding a new node:*
    <br> newnode <node_name> <node_id> 
        - Ex: ```newnode n1 30```
    - *Joining a node to DHT:*
    <br> join <new_node_name> <existing_node_name>
        - Ex: ```join n1 n0```
    - *pretty print fingerTable of a node:*
    <br> prettyprintFinger <node_name>
        - Ex: ```prettyprintFinger n0```
    - *insert key into DHT from a given node:*
    <br> insert <node_name> <key> <value>
        - Ex: ```insert n0 3 3```
        or
        - Ex: ```insert n0 200``` Here the value is assumed as None
    - *pretty print key value pairs stored in all nodes:*
    <br> prettyprintKeys <node_name>
        - Ex: ```prettyprintKeys n0```
    - *look up all keys from a given node:*
    <br> lookupall <node_name>
        - Ex: ```lookupall n2```
    - *find value of a key from a given node*
    <br> find <node_name> <key>
        - Ex: ```find n0 3```
    - *remove a key from DHT from a given node*
    <br> remove <node_name> <key>
        - Ex: ```remove n1 3```

### **Files:**
- main.py -> main file which needs to executed
- Node.py -> contains class Node and its functions.
- FingerTable.py -> contains class fingerTable and its functions.
- testcase.txt -> sample testcases.
