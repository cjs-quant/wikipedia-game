
# FILE: wikipedia_game.py
# AUTHOR: Christopher Simard
# DESCRIPTION: plays wikipedia given start and end wikipedia pages
# ARGUMENTS:
#   page_start: starting page for game
#   page_end: ending page for game

# load libraries
import pandas as pd
import wikipedia
import time

# load structures
from structures import *

# play game
start = time.time()
def wikipedia_game(page_start, page_end):
    # check if start page exists
    try:
        wikipedia.page(page_start)
    except:
        print('Start page does not exist.')
        return

    # check if end page exists
    try:
        wikipedia.page(page_end)
    except:
        print('End page does not exist.')
        return

    # initialize tree object
    tree = Tree(page_start)

    # plays game
    i = 0
    links_all = []
    a = []
    while a != page_end:

        # collect nodes in tree level
        level = list(tree.get_level_nodes(i))

        # loop over nodes in level
        for j in level:

            # ends game if eng_page found
            if a == page_end:
                break

            try:
                temp = wikipedia.page(j.name)
            except:
                pass
            links = list(set(temp.links) - set(links_all))
            links_all = links_all + links

            # add links as new children
            m = 0
            for k in links:
                j.add_child(k)
                if k == page_end:
                    page_current = j.children[m]
                    a = page_current.name
                    break
                m = m + 1

        # iterate level
        i = i + 1

    # recover path
    path = page_current.get_path()
    path.reverse()

    # compute game time
    end = time.time()
    delta = end - start

    # return # of clicks and time of game
    print(page_end, "found in", page_current.level, "clicks, over %1.2f seconds!" % delta)
    print("The path to find", page_end, "is:", (', '.join(path)))
