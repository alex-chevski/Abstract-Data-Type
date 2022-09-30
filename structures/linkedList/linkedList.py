#!/usr/bin/env Python3
from structures.linkedList.Node import Node


class linked_list(object):

    def __init__(self, node=None):
        self.head = node

    def append_node(self, data):
        new_node = Node(data)
        head_node = self.head

        isHeadNone = lambda head: True if head is None else False

        if isHeadNone(head_node):
            self.head = new_node
            return

        curr_node = head_node

        while curr_node.next is not None:

            curr_node = curr_node.who_next

        curr_node.who_next = new_node

    def show_all_nodes(self):

        curr_node = self.head

        nodes = []

        while curr_node is not None:
            nodes.append(curr_node.data_of_node)
            curr_node = curr_node.who_next
        print(nodes)

    def length_list(self):
        curr_node = self.head
        length = 0

        while curr_node is not None:
            curr_node = curr_node.who_next
            length += 1
        return length

    def push_front_node(self, data):
        new_node = Node(data)
        curr_node = self.head

        new_node.who_next = curr_node
        self.head = new_node

    def erase_back_node(self):
        curr_node = self.head

        while curr_node.who_next.who_next is not None:
            curr_node = curr_node.who_next

        curr_node.who_next = None

    def erase_front_node(self):
        curr_node = self.head
        self.head = curr_node.who_next

    def data_at_index_list(self, index):
        curr_node = self.head
        count = 0

        while curr_node is not None:
            isEqualIndexWithCount = lambda count: True if count == index else False

            if isEqualIndexWithCount(count):
                return curr_node.data_of_node
            else:
                count += 1
                curr_node = curr_node.who_next
        else:
            return None

    def insert_node_at_index(self, index, data):
        curr_node = self.head
        new_node = Node(data)
        count = 0

        while curr_node is not None:

            if index == 0:
                self.push_front_node(data)
                return
            elif index == count + 1:
                tmp = curr_node.who_next
                curr_node.who_next = new_node
                new_node.who_next = tmp
                return
            count += 1

            curr_node = curr_node.who_next
        else:
            return None
