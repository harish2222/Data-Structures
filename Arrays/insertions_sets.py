def intersect_method(first_arr, second_arr):
    i = 0
    j = 0
    intersection = []

    while i < len(first_arr) and j < len(second_arr):
        if first_arr[i] == second_arr[j]:
            if i == 0 or first_arr[i] != first_arr[i - 1]:
                intersection.append(first_arr[i])
            i += 1
            j += 1
        elif first_arr[i] < second_arr[j]:
            i += 1
        else:
            j += 1
    return intersection


def union_method(first_arr, second_arr):
    for i in first_arr:
        if i not in second_arr:
            second_arr.append(i)
    res = [i for n, i in enumerate(second_arr) if i not in second_arr[:n]]
    return sorted(res)


if __name__ == '__main__':
    A = [2, 3, 3, 5, 7, 11]
    B = [3, 3, 7, 15, 31]

    print(set(A).intersection(B))
    print(set(A).union(B))
    c = intersect_method(A, B)
    d = intersect_method(B, A)
    print(c)
    print(d)
    e = union_method(A, B)
    print(e)
