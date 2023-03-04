# python3

#Dāvis Zommers 221RDB150 7.grupa

from itertools import combinations_with_replacement
import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    for i in range (len(parents)):
        if (parents[i] == n):
            childHeight = compute_height(i, parents)
            if (childHeight > max_height):
                max_height = childHeight
    return max_height + 1


def main():
    # implement input form keyboard and from files

    choice = input()
    n = int(input())
    if ("I" in choice):
        #n = int(input())
        elements = numpy.array(input().split())
    #D:/testfails.txt
    if ("F" in choice):
        print("Input file path")
        while True:
            path = input()
            if ("a" not in path.lower()):
                #print("File not allowed")
            #else:
                f = open(path, "r")
                elements = numpy.array(f.read().split())
                f.close()
                break

    parents = []
    try:
        for i in range(0, n):
            if (-1 <= int(elements[i]) and int(elements[i]) <= n-1):
                parents.append(int(elements[i]))
            else:
                break

        root = parents.index(-1)

        height = compute_height(root, parents)
        print(height)
    except:
        print("error")
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    #pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))
