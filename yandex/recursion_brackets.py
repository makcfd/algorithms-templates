# функция gen_binary(n, prefix):
#     if n == 0:
#         print(prefix)
#     else:
#         gen_binary(n - 1, prefix + '0')
#         gen_binary(n - 1, prefix + '1')  


# def gen_binary(n, prefix):
#     if n == 0:
#         return [prefix]
#     else:
#         result = []
#         result += gen_binary(n - 1, prefix + '0')
#         result += gen_binary(n - 1, prefix + '1')
#         return result


# def test():
#     assert gen_binary(2, "") == ['00', '01', '10', '11']


# test()


def gen_brackets(n: int):
    answer = []
    left_count = 0
    right_count = 0

    def backtracking(cur_string, left_count, right_count):
        if len(cur_string) == 2*n:
            answer.append(cur_string)
        if left_count < n:
            new_string = cur_string + '('
            backtracking(new_string, left_count + 1, right_count)
        if left_count > right_count:
            new_string = cur_string + ')'
            backtracking(new_string, left_count, right_count + 1)
    backtracking("", left_count, right_count)
    return answer



if __name__ == "__main__":
    n = int(input())
    for item in gen_brackets(n):
        print(item)
