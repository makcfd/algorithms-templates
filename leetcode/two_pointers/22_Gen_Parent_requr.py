def generateParenthesis(n):
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


def test():
    assert generateParenthesis(2) == ['(())', '()()']


if __name__ == '__main__':
    test()