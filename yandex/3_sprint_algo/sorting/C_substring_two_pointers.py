test = """m
zzkqxfdxbbjqhatygmtmpgbhumicrhtjkrfblwwnjlebsfdawznznxwyzehpubvdukmgwrivygosfkdquwxvkvtfvwjfwtvjvtplpckktmnhfnxprjetpxnddoiiqotzrjjfdwnzdjvtclcqwsvsegnuajookwppzfsf""".split("\n")


def input():
    return test.pop(0)


def is_substring(s, t):
    l, r = len(s), len(t)
    p_l, p_r = 0, 0
    while p_l < l and p_r < r:
        if s[p_l] == t[p_r]:
            p_l += 1
        p_r += 1
    return p_l == l


if __name__ == "__main__":
    source = input()
    target = input()
    print(is_substring(source, target))
