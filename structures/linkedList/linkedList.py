#!/usr/bin/env Python3
from structures.linkedList.Node import Node


class linked_list:

    def __init__(self):
        self.head = None

    def append(self, data):

        new_node = Node(data)
        curr_node = self.head

        isHeadNodeNone = lambda curr_node: True if curr_node is None else False

        if isHeadNodeNone(curr_node):
            self.head = new_node
            return
        else:
            while curr_node.get_next() is not None:
                curr_node = curr_node.get_next()

            curr_node.set_next(new_node)

    def show(self):
        curr_node = self.head
        output = []

        while curr_node is not None:
            output.append(curr_node.get_data())
            curr_node = curr_node.get_next()

        print(output)
