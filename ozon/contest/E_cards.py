input_data = """5 7
3 3 2 6 5""".split('\n')


def input():
    global input_data
    return input_data.pop(0)


def gift_cards(num_cards, friends_cards):
    cards_to_gift = [i for i in range(num_cards + 1)]
    friends_cards = sorted(friends_cards)
    final = []
    for card in friends_cards[::-1]:
        for new_card in cards_to_gift[::-1]:
            if new_card > card:
                final.append(new_card)
                cards_to_gift.pop()
                friends_cards.pop()
    print(final)


if __name__ == "__main__":
    num_friends, num_cards = [int(i) for i in input().strip().split()]
    friends_cards = [int(i) for i in input().strip().split()]
    gift_cards(num_cards, friends_cards)
