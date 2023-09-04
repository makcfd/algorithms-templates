
from collections import deque


search_queue = deque()

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anju', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anju'] = []
graph['peggy'] = []
graph['jonny'] = []

search_queue += graph['you']


def person_is_seller(person):
    return person[-1] == 'm'


while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(True)
    else:
        search_queue += graph[person]
print(False)
