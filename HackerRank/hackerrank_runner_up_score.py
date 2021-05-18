# hackerrank_runner_up_score


def main(n: str) -> int:
    arr = map(int, n.split())

    return sorted(list(set(arr)))[-2]


print(main("57 57 -57 57"))
