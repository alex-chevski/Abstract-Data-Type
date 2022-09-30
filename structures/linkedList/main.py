#!/usr/bin/env python3
from structures.linkedList.linkedList import linked_list

my_list = linked_list()

my_list.append_node(2)
my_list.append_node(4)
my_list.append_node(8)
my_list.append_node(16)
my_list.append_node(24)

my_list.show_all_nodes()

my_list.push_front_node(17)

my_list.show_all_nodes()

print(my_list.length_list())

my_list.erase_back_node()
my_list.erase_back_node()
my_list.show_all_nodes()

my_list.erase_front_node()

my_list.show_all_nodes()

print(my_list.data_at_index_list(0))

my_list.insert_node_at_index(2, 16)

my_list.show_all_nodes()
