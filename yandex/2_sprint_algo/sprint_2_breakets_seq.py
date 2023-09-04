test = "({})({[]}[])"


def is_correct_brackets(text):
    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')
    return not text




print(is_correct_brackets(test))

# def is_correct_bracket_seq(seq: str) -> bool:
#     if not len(seq) % 2:
#         split_idx = int(len(seq)/2)
#         for left_element, right_element in zip(seq[:split_idx], seq[:split_idx-1:-1]):
#             print(f"left: {left_element}, right: {right_element}")


#     #         if seq[index] == seq[-index]:
#     #             continue
#     #         else:
#     #             return False
#     #     return True
#     # return False


# if __name__ == "__main__":
#     print(is_correct_bracket_seq(test))
