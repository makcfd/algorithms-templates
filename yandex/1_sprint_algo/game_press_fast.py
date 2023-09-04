"""
ID of package:
    89650681.

Description:
    The "Speed Typing Trainer" is a square a sixteen-key 4x4 keyboard.
    Each key can have either a dot, or a number from 1 to 9.
    1 point is received for having pressed all available buttons,
    taking into account the limit of k

Args:
    max_keys_to_press (int): 1 ≤ max_keys_to_press ≤ 5,
                             max number of buttons that
                             ONE participant can press.
    matrix (int): Round number and keys to press.

Returns:
    points (int): Number of points received by the players.
"""


def count_points_in_game(max_keys_to_press, matrix):
    freq_count = {}
    [freq_count.update({num: freq_count.get(num, 0) + 1}) for num in matrix]
    points = (sum(1 for value in range(1, 10)
                  if max_keys_to_press >= freq_count.get(str(value), 11)))
    return points


if __name__ == "__main__":
    max_keys_to_press = int(input()) * 2
    matrix = "".join([input() for _ in range(4)])
    print(count_points_in_game(max_keys_to_press, matrix))
