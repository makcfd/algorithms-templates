test = """8 10
1 2
1 3
1 4
4 3
3 2
2 4
1 8
5 6
7 6
5 7""".split('\n')


def input():
    global test
    return test.pop(0)


if __name__ == "__main__":
    num_users, num_pairs = [int(i) for i in input().split()]
    friends = {i: set() for i in range(1, num_users + 1)}
    for i in range(num_pairs):
        x, y = [int(i) for i in input().split()]
        friends[x].add(y)
        friends[y].add(x)

    for user in range(1, num_users + 1):
        common_friends = {}
        for friend in friends[user]:
            for friend_of_friend in friends[friend]:
                if friend_of_friend not in friends[user] and friend_of_friend != user:
                    inter = friends[user].intersection(friends[friend_of_friend])
                    if inter:
                        common_friends[friend_of_friend] = len(inter)
        max_common = max(common_friends.values(), default=0)
        possible_friends = sorted([k for k, v in common_friends.items() if v == max_common])
        if possible_friends:
            print(*possible_friends)
        else:
            print(0)
