from utils import read_num_data_into_sorted_lists, num_times_in_list

class DataException(Exception):
    pass


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
    list1, list2 = read_num_data_into_sorted_lists("inputs/p1.txt")
    print(diff_of_lists(list1, list2))
    print(similarity_of_lists(list1, list2))


if __name__ == "__main__":
    main()