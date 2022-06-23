#!/usr/bin/python3
""" Node module """


class Node:
    """ Defines a node of a singly linked list """

    def __init__(self, data, next_node=None) -> None:
        """Initializes attributes

        Args:
            data: value in each node in a list
            next_node: address of next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Gets node data """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ Gets next node of the linked list"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """ Defines a singly linked list """

    def __init__(self) -> None:
        """ Initialize attributes """
        self.__head = None

    def __str__(self) -> str:
        """ returns string to be printed """
        result = list()
        nxt = self.__head

        while nxt is not None:
            result.append(str(nxt.data))
            nxt = nxt.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Sorts node of the list in ascending order of data

        Args:
            value: value of each node in the list
        """
        # create node if none exists
        if self.__head is None:
            self.__head = Node(value, None)
            return

        # sets node at beginning
        if value < self.__head.data:
            self.__head = Node(value, self.__head)
            return

        prev, nxt = self.__head, self.__head.next_node
        # sets node between nodes
        while nxt is not None:
            if value < nxt.data:
                prev.next_node = Node(value, nxt)
                return
            prev = nxt
            nxt = nxt.next_node
        prev.next_node = Node(value, None)
