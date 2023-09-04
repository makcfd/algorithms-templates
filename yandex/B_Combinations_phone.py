def get_combinations(numbers: str):
    symbols = {'2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'pqrs',
               '8': 'tuv',
               '9': 'wxyz'}
    ans = []
    def backtrack(i, curStr):
        # basecase
        if len(numbers) == len(curStr):
            ans.append(curStr)
            return
        for char in symbols[numbers[i]]:
            backtrack(i + 1, curStr + char)
    if numbers:
        backtrack(0, '')
        return ans



stng = "23"
print(get_combinations(stng))
