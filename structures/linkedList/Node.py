#!/usr/bin/env Python3


class Node(object):

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    @property
    def data_of_node(self):
        return self.data

    @data_of_node.setter
    def data_of_node(self, data):
        self.data = data

    @property
    def who_next(self):
        return self.next

    @who_next.setter
    def who_next(self, next):
        self.next = next
