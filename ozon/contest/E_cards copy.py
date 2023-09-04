input_data = """5 7
3 3 2 6 5""".split('\n')


def input():
    global input_data
    return input_data.pop(0)


def gift_cards(num_cards, friends_cards):
    cards_to_gift = set(range(1, num_cards + 1))
    final = []
    for card in friends_cards:
        gift = min(cards_to_gift - set(range(1, card + 1)))
        final.append(gift)
        cards_to_gift.remove(gift)
    return final


if __name__ == "__main__":
    num_friends, num_cards = [int(i) for i in input().strip().split()]
    friends_cards = [int(i) for i in input().strip().split()]
    result = gift_cards(num_cards, friends_cards)
    print(-1) if result == -1 else print(' '.join(str(i) for i in result))
