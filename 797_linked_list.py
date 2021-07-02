class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._list = []
        self._len = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        return -1 if index >= self._len else self._list[index]


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self._list = [val] + self._list
        self._len += 1


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self._list += [val]
        self._len +=1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index<self._len-1:
            self._list.insert(index, val)
            self._len +=1
        else:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < self._len:
            self._list.pop(index)
            self._len-=1

    def printList(self):
        print(self._list,self._len)


# Your MyLinkedList object will be instantiated and called as such:


obj = MyLinkedList()
obj.printList(); 
param_1 = obj.addAtHead(5)
obj.printList(); 
param_1 = obj.addAtIndex(1,2)
obj.printList(); 
param_1 = obj.get(1)
obj.printList(); 
param_1 = obj.addAtHead(6)
obj.printList(); 
param_1 = obj.addAtTail(2)
obj.printList(); 
param_1 = obj.get(3)
obj.printList(); 
param_1 = obj.addAtTail(1)



obj.printList(); 
param_1 = obj.get(5)
obj.printList(); 
param_1 = obj.addAtHead(2)
obj.printList(); 
param_1 = obj.get(2)
obj.printList(); 
param_1 = obj.addAtHead(6)
