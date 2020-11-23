start = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
#Sắp xếp thời gian kết thúc theo thứ tự.
finish = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

def greedy_activity_selector(s, f):
    assert(len(s) == len(f))  # each start time must match a finish time
    n = len(s)  # could be len f as well!
    a = []
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            a.append(m)
            k = m
    return a
print(greedy_activity_selector(start,finish))