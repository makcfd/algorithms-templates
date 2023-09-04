# col = 1
# matrix = [
#     [6, 2, 3],
#     [4, 0, 1],
#     [5, 9, 8]
# ]

# # Отсортировать матрицу по второй колонке (индекс 1)
# sorted_matrix = sorted(matrix, key=lambda row: row[col])

# print(sorted_matrix)

# task <> previous_task -> good
# task == previous_task -> good
# task == task+2 -> bad
# l1 = ["a", "b", "c", "d","a"]
# efficient = True
# for el_idx in range(len(l1)):
#     el = l1[el_idx]
#     if el_idx != el_idx+1 and el in l1[el_idx+1:]:
#         efficient = False
#         break
# print(efficient)
"""
approach
if task <> next task and task in list -> bad
"""

l1 = ["a", "c" ,"c", "d", "c"]
seen = set()
efficient = True
# start with second element in list
for i in range(1, len(l1)):
    # check of second element have been seen?
    if l1[i] in seen:
        # if so, worker is not efficient
        efficient = False
        break
    # if element has not been seen we check if previous 
    # element is the same
    if l1[i] != l1[i-1]:
        # if it is not the same we add previous element
        # to seen set
        seen.add(l1[i-1])
print(efficient)

seen = set()

time_slot = "00:00:00-23:59:58"
for slot in time_slot.split("-"):
    hour, min, sec = [int(i) for i in slot.split(":")]
    print(hour, min, sec)


list_of_sets = [{3, 1, 2}, {5, 4, 6}, {8, 7, 9}]

# Convert each set to a sorted tuple and sort the list of tuples
sorted_list_of_tuples = sorted([tuple(sorted(s)) for s in list_of_sets])

print(sorted_list_of_tuples)


