# hackerrank_nested_lists

if __name__ == '__main__':

    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        grades.append([name, score])
    # dict(grades.sort(key = lambda x: x[1]))
    # sorted_grades = sorted(grades, key = lambda x: x[1])
    penultimate = sorted(list(set(sublist[1] for sublist in grades)))[1]
    names = sorted([sublist[0]
                   for sublist in grades if sublist[1] == penultimate])
    for i in names:
        print(i)
