# Darren Good, Tyler Huffman
# 2020-03-04
# https://open.kattis.com/problems/tarifa

from sys import stdin
print(int(input()) * (int(input()) + 1) - sum([int(x) for x in stdin.read().strip().split()]))