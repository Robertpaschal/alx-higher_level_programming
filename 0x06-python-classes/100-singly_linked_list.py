#!/usr/bin/python3
"""A Singly Linked list Module """


class Node:
    """
    This class represents a node of a singly linked list.

    Attributes:
        __data: Private instance attribute representing the data of the node.
        __next_node: Private instance attribute \
                representing the next node in the linked list.

    Methods:
        __init__: Initializes a Node object with data and optional next_node.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a Node object with data and optional next_node.

        Parameters:
            data (int): The data of the node.
            next_node (Node): The next node in the linked list.\
                    Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data of the node.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.

        Parameters:
            value (int): The data to set.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the next node in the linked list.

        Returns:
            Node or None: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the next node in the linked list.

        Parameters:
            value (Node or None): The next node to set.

        Raises:
            TypeError: If next_node is not a Node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Attributes:
        __head: Private instance attribute\
                representing the head of the linked list.

    Methods:
        __init__: Initializes a SinglyLinkedList object.
        sorted_insert: Public instance\
                method that inserts a new Node \
                into the correct sorted position.
    """

    def __init__(self):
        """
        Initializes a SinglyLinkedList object with an empty head.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct \
                sorted position in the list (increasing order).

        Parameters:
            value (int): The value to insert.
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None \
                    and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: String representation of the linked list.
        """
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.strip()
