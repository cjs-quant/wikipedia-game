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

    # initialize search
    i = 0
    clicks = 0
    q = pd.DataFrame({'page': [page_start], 'clicks': [clicks]})
    page_current = page_start

    # plays game
    while page_current != page_end:

        # find new links in current page
        try:
            page = wikipedia.page(q.page[i])
            page_current = page.title
            links = page.links
            links = list(set(links) - set(q.page))

            # check if end page exists in new links
            if page_end in links:
                page_current = page_end

            # if end page not in links, append new links to queue
            links = pd.DataFrame({'page': links, 'clicks': [q.clicks[i] + 1] * len(links)})
            q = q.append(links, ignore_index=True)

            # load next page
            i = i + 1
        except:
            pass

    # compute game time
    end = time.time()
    delta = end - start

    # return # of clicks and time of game
    print(page_end, "found in", q.clicks[i] + 1, "clicks, over %1.2f seconds!" % delta)
