

def read_num_data_into_sorted_lists(filename: str) -> (list, list):
    list1 = []
    list2 = []
    with open(filename, "r") as f:
        for line in f:
            n1, n2 = line.strip().split()
            list1.append(int(n1))
            list2.append(int(n2))

    return sorted(list1), sorted(list2)


def num_times_in_list(some_list: list) -> dict:
    results = {}
    for each in some_list:
        if results.get(each):
            results[each] += 1
        else:
            results[each] = 1
    return results