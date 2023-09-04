input_data = """4
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
    base_temp = [i for i in range(0, 31)]
    while temp_requests:
        req = temp_requests.pop()
        condtn = req[0]
        temp = int(req[1])
        if condtn == '<=':
            temp += 1
            base_temp = base_temp[:temp]
            print(max(base_temp) if base_temp else -1)
        else:
            base_temp = base_temp[temp:]
            print(max(base_temp) if base_temp else -1)


if __name__ == "__main__":
    sets = int(input())
    for set in range(sets):
        num_planktone = int(input())
        temp_requests = [input().strip().split() for _ in range(num_planktone)][::-1]
        find_temp(temp_requests)
