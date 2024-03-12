#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data=value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None or isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node and current_node.next_node.data < value:
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = current_node.next_node

    def __str__(self):
        result = ""
        current_node = self.head
        while current_node:
            result += str(current_node.data) + " -> "
            current_node = current_node.next_node
        result += "None"
        return result
