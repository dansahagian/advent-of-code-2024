from pathlib import Path

from settings import DATA_PATH


class DataException(Exception):
    pass


def parse_data(filename: Path) -> (list, list):
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


def diff_of_lists(list1: list, list2: list) -> int:
    l1 = len(list1)
    l2 = len(list2)

    if l1 != l2:
        raise DataException

    return sum([abs(list1[i] - list2[i]) for i in range(l1)])


def similarity_of_lists(list1: list, list2: list) -> int:
    list2_counts = num_times_in_list(list2)
    score = 0
    for each in list1:
        m = list2_counts.get(each, 0)
        score += each * m

    return score


def main():
    list1, list2 = parse_data(DATA_PATH / "day_01.txt")
    print(diff_of_lists(list1, list2))
    print(similarity_of_lists(list1, list2))


if __name__ == "__main__":
    main()
