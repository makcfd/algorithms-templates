"""
6
2 1 3 1 1 4
"""


def sort_table(matrix: list, num_clicks: int, clicked_cols_idx: list):
    for click in range(num_clicks):
        col = clicked_cols_idx[click]
        matrix = sorted(matrix, key=lambda row: row[col])
    print(matrix)


if __name__ == "__main__":
    iterations = int(input())
    for iter in range(iterations):
        print()
        matrix = []
        rows, cols = [int(i) for i in input().strip().split()]
        for row in range(rows):
            row_vals = [int(i) for i in input().strip().split()]
            matrix.append(row_vals)
        num_clicks = int(input())
        clicked_cols_idx = [int(i)-1 for i in input().strip().split()]
        sort_table(matrix, num_clicks, clicked_cols_idx)
