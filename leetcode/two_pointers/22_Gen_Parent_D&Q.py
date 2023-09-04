def generateParenthesis(n):
    if n == 0:
        return ['']
    answer = []
    for left_count in range(n):
        for left_string in generateParenthesis(left_count):
            for right_string in generateParenthesis(n - 1 - left_count):
                answer.append('(' + left_string + ')' + right_string)
    return answer


def test():
    assert generateParenthesis(2) == ['(())', '()()']


if __name__ == '__main__':
    test()
