#!/usr/bin/python3
"""
Script
"""

import sys
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

args = sys.argv[1:]

file = "add_item.json"

if os.path.exists(file):
    my_list = load_from_json_file(file)
else:
    my_list = []

my_list.extend(args)
save_to_json_file(my_list, file)
