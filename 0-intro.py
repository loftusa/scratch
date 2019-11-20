#%%
from typing import List
# base data
names = [
    "Hero",
    "Dunn",
    "Sue",
    "Chi",
    "Thor",
    "Clive",
    "Hicks",
    "Devin",
    "Kate",
    "Klein",
]
ids = range(len(names))

# built-upon data
users = [{"id": id, "name": name} for id, name in zip(ids, names)]
friendship_pairs = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 8),
    (7, 8),
    (8, 9),
]

## dict where keys are ids and values are lists of friend ids ##
# e.g., {0: [1, 2], 1: [2, 3], ...,}

# My way: no duplicate information
friendships = {
    id: [pair[1] for pair in friendship_pairs if id == pair[0]] for id in ids
}

# Joel's way: contains duplicate information
friendships = {id: [] for id in ids}
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)


## what's the average number of connections? ##

# my way
total_connections = sum([len(value) for value in friendships.values()])
average_connections = total_connections / len(friendships)
average_connections

# Joel's way
def number_of_friends(user):
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)


total_connections = sum(number_of_friends(user) for user in users)
average_connections = total_connections / len(users)

## find the most connected people ##
## by sorting from "most friends" to "least friends ##
# my way
unsorted_num_friendships = {name: len(friendships[i]) for i, name in enumerate(names)}
sorted_num_friendships = [
    (name, unsorted_num_friendships[name])
    for name in sorted(
        unsorted_num_friendships, key=unsorted_num_friendships.get, reverse=True
    )
]

# Joel's way
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)

# make a friendships adjacency matrix
# [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
#  [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
#               ...,
#                               ]]
adjacency_matrix = []
for user_id in friendships:
    # initiate list with default 0's
    row = [0 for i, _ in enumerate(friendships)]
    for i, _ in enumerate(row):
        if i in friendships[user_id]:
            row[i] += 1
    adjacency_matrix.append(row)
adjacency_matrix  # yeet

friendship_pairs
friendships
users
adjacency_matrix
num_friends_by_id  # degree centrality

# define function that finds friends of friends
# e.g., friends_of_friends("Hero")
# >> [0, 2, 3, 0, 1, 3]
# My way -- dont like it, too nested
def friends_of_friends(user: str) -> List[int]:
    index = names.index(user)
    foafs: List[int] = []
    for id, binary in enumerate(adjacency_matrix[index]):
        if binary:
            for fid, fbin in enumerate(adjacency_matrix[id]):
                if fbin:
                    foafs.append(fid)
    return foafs

friends_of_friends("Hero")

# # Joel's way
# # TODO : bugged
# def friends_of_friends(user):
#     foafs: List[int] = []
#     for friend_id in friendships[user["id"]]:
#         for foaf_id in friendships[friend_id]:
#             foafs.append(foaf_id)
#     return foafs

## To Be Continued