from settings import DATA_PATH


def parse_data() -> tuple[str, str]:
    with open(DATA_PATH / "day_05.txt", "r") as f:
        data = f.read()

    rules, reprints = data.split("\n\n")
    return rules, reprints


def create_rules_map(rules: str) -> dict:
    rules_map = {}
    for rule in rules.split():
        before, after = rule.split("|")
        before = int(before)
        after = int(after)

        if rules_map.get(before):
            rules_map[before]["before"].add(after)
        else:
            rules_map[before] = {"before": {after}, "after": set()}

        if rules_map.get(after):
            rules_map[after]["after"].add(before)
        else:
            rules_map[after] = {"after": {before}, "before": set()}

    return rules_map


def check_reprint_order(order: list[int], rules: dict) -> bool:
    for i, current_page in enumerate(order):
        for page in order[i + 1 :]:
            if (
                rules.get(current_page)
                and rules[current_page].get("after")
                and page in rules[current_page]["after"]
            ):
                return False
    return True


def correct_order(order: list, rules: dict) -> list:
    for i in range(len(order) - 1):
        p1 = order[i]
        p2 = order[i + 1]
        if rules.get(p1) and rules[p1].get("after") and p2 in rules[p1]["after"]:
            order.pop(i + 1)
            order.insert(i, p2)
    if check_reprint_order(order, rules):
        return order
    return correct_order(order, rules)


def check_reprints() -> tuple[int, int]:
    rules, reprints = parse_data()
    rules = create_rules_map(rules)

    sum_of_correct_middle_pages = 0
    sum_of_corrected_middle_pages = 0
    for reprint in reprints.split():
        order = [int(x) for x in reprint.split(",")]
        if check_reprint_order(order, rules):
            sum_of_correct_middle_pages += order[len(order) // 2]
        else:
            corrected_order = correct_order(order, rules)
            sum_of_corrected_middle_pages += corrected_order[len(order) // 2]

    return sum_of_correct_middle_pages, sum_of_corrected_middle_pages


if __name__ == "__main__":
    print(check_reprints())
