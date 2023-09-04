from collections import defaultdict

test = """8 6
4 3
3 1
1 2
2 4
2 5
6 8""".split('\n')

test_2 = """8 10
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
    #for user in range(1, 9):
        common_friends = {}
        for key, value in friends.items():
            if key != user:
                inter = friends[user].intersection(friends[key])
                if inter:
                    #print(f"Looking into pairs: {user}, {key}")
                    common_friends[key] = len(inter)
        max_common = max(common_friends.values(), default=0)
        possible_friends = sorted([k for k, v in common_friends.items() if v == max_common])
        #print(f"for user {user} possible friends")
        if possible_friends:
            print(*possible_friends)
        else:
            print(0)
        #[print(" ".join(str(i))) for i in possible_friends] if possible_friends else print("0")
                # print(f"user data: {friends[user]} , key data: {friends[key]}")
                # print()
                # print("intersection is: ", friends[user].intersection(friends[key]))
    #     common_friends = [friends[user].intersection(friends[key]) for key in friends.keys() if key != user]
    # print(common_friends)


    # for user in range(1, num_users + 1):
    #     common_friends = defaultdict(int)
    #     user_friends = friends[user]
    #     for friend in user_friends:
    #         friends_of_user_friend = friends[friend]
    #         for friend_of_friend in friends_of_user_friend:
    #             if friend_of_friend not in friends[user] and friend_of_friend != user:
    #                 common_friends[friend_of_friend] += 1
    #     max_common = max(common_friends.values(), default=0)
    #     possible_friends = sorted([k for k, v in common_friends.items() if v == max_common])
    #     if possible_friends:
    #         print(" ".join(map(str, possible_friends)))
    #     else:
    #         print(0)
