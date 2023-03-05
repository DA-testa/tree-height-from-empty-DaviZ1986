# python3

#Dāvis Zommers 221RDB150 7.grupa

from itertools import combinations_with_replacement
import sys
import threading
import numpy


def compute_height(n, parents):
    heights = [0] * len(parents)
    for i in range(len(parents)):
        if heights[i] != 0:
            continue
        height = 0
        j = i
        while j != -1:
            if heights[j] != 0:
                height += heights[j]
                break
            height += 1
            j = parents[j]
        heights[i] = height
    return max(heights) + 1


def main():
    choice = input()
    if ("I" in choice):
        n = int(input())
        elements = numpy.array(list(map(int, input().split())))
    if ("F" in choice):
        print("Input file path")
        path = input()
        path = "./test/" + path
        if ("a" not in path.lower()):
            f = open(path, "r")
            n = int(f.readline())
            elements = numpy.array(list(map (int, f.readline().split())))
            f.close()

    for i in range(n):
            if int(elements[i]) == -1:
                root = elements[i]

    height = compute_height(root, elements)
    print(height - 1)
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
