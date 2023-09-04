input_data = """4
1
>= 30
6
>= 18
<= 23
>= 20
<= 27
<= 21
>= 28
3
<= 25
>= 20
>= 25
3
<= 15
>= 30
<= 24""".split('\n')


def input():
    global input_data
    return input_data.pop(0)

def find_temp(temp_requests):
    min_temp, max_temp = 15, 30
    while temp_requests:
        req = temp_requests.pop()
        condtn, temp = req[0], int(req[1])
        if condtn == '<=':
            max_temp = min(max_temp, temp)
        else:
            min_temp = max(min_temp, temp)
        if min_temp <= max_temp:
            print(max_temp)
        else:
            print(-1)

if __name__ == "__main__":
    sets = int(input())
    for _ in range(sets):
        num_planktone = int(input())
        temp_requests = [input().strip().split() for _ in range(num_planktone)][::-1]
        find_temp(temp_requests)
        print()
