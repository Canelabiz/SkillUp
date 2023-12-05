def f1(
    schedule: list[list] = [[1, 2, 2, 4, 1], [1, 5, 6, 9, 3], [6, 3, 4, 5, 1]]
) -> int:
    multi_hosp_doc = []
    for idx, hospital in enumerate(schedule):
        other_hospitals = schedule.copy()
        other_hospitals.pop(idx)
        other_hospitals = [doc for hosp in other_hospitals for doc in hosp]
        for doctor in set(hospital):
            if doctor in other_hospitals:
                multi_hosp_doc.append(doctor)
    return len(set(multi_hosp_doc))


def f2(
    schedule: list[list] = [[1, 2, 2, 4, 1], [1, 5, 6, 9, 3], [6, 3, 4, 5, 1]]
) -> int:
    multi_hosp_doc = []
    for idx, hospital in enumerate(schedule):
        other_hospitals = schedule.copy()
        other_hospitals.pop(idx)
        other_hospitals = {doc for hosp in other_hospitals for doc in hosp}
        for doctor in set(hospital):
            if doctor in other_hospitals:
                multi_hosp_doc.append(doctor)
    return len(set(multi_hosp_doc))


def f3(
    schedule: list[list] = [[1, 2, 2, 4, 1], [1, 5, 6, 9, 3], [6, 3, 4, 5, 1]]
) -> int:
    multi_hosp_doc = []
    for idx, hospital in enumerate(schedule):
        other_hospitals = schedule.copy()
        other_hospitals.pop(idx)
        other_hospitals = {doc for hosp in other_hospitals for doc in hosp}
        multi_hosp_doc.extend(
            doctor for doctor in set(hospital) if doctor in other_hospitals
        )
    return len(set(multi_hosp_doc))


def f4(
    schedule: list[list] = [[1, 2, 2, 4, 1], [1, 5, 6, 9, 3], [6, 3, 4, 5, 1]]
) -> int:
    multi_hosp_doc = []
    for idx, hospital in enumerate(schedule):
        other_hospitals = schedule.copy()
        other_hospitals.pop(idx)
        other_hospitals = {doc for hosp in other_hospitals for doc in hosp}


def f5(
    schedule: list[list[int]] = [[1, 2, 2, 4, 1], [1, 5, 6, 9, 3], [6, 3, 4, 5, 1]]
) -> int:
    docs = [doc for hosp in schedule for doc in set(hosp)]
    return len({doc for doc in docs if docs.count(doc) > 1})


if __name__ == "__main__":
    import timeit

    print(f2())
    print(f5())
    print(timeit.timeit(f1, number=10000))
    print(timeit.timeit(f2, number=10000))
    print(timeit.timeit(f3, number=10000))
    # print(timeit.timeit(f4, number=10000))
    print(timeit.timeit(f5, number=10000))
