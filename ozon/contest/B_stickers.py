input_data = """somesuperlongstring
3
1 2 la
4 4 d
10 13 tiny""".split('\n')

input_data_2 = """somesuperlongstring
4
1 2 la
4 4 d
10 13 tiny
4 5 ed""".split('\n')


def input():
    global input_data_2
    return input_data_2.pop(0)


def modify_stickers(sticker, modifications):
    while modifications:
        modification = modifications.pop()
        start_idx = int(modification[0]) - 1
        #print("start_idx: ", start_idx)
        end_idx = int(modification[1])
        #print("end_idx: ", end_idx)
        insert = modification[2]

        # print("first part: ", sticker[:start_idx])
        # print("second part: ", sticker[end_idx:])
        sticker = sticker[:start_idx] + insert + sticker[end_idx:]
    print(sticker)

if __name__ == "__main__":
    original_sticker = input().strip()
    num_modifications = int(input())
    modifications = [input().strip().split() for _ in range(num_modifications)][::-1]
    modify_stickers(original_sticker, modifications)
