# Darren Good, Tyler Huffman
# 2020-03-04
# https://open.kattis.com/problems/qaly

from sys import stdin
print(sum([float(inp_str.split()[0]) * float(inp_str.split()[1]) for inp_str in stdin.read().strip().split('\n')[1:]]))