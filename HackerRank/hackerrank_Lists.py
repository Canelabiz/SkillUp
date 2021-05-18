# hackerrank Lists

if __name__ == '__main__':
    # N = int(input())
    # commands = [input().split() for i in range(N)]
    commands = [['insert', '0', '5'], ['insert', '1', '10'], ['insert', '0', '6'], ['print'], [
        'remove', '6'], ['append', '9'], ['append', '1'], ['sort'], ['print'], ['pop'], ['reverse'], ['print']]
    leest = []
    # insert i e: Insert integer e at position i
    # print: Print the list.
    # remove e: Delete the first occurrence of integer e
    # append e: Insert integer e at the end of the list.
    # sort: Sort the list.
    # pop: Pop the last element from the list.
    # reverse: Reverse the list.

    # dict will not work due to repeated commands
    # d_com = {command[0]: command[1:] for command in commands}

    for command in commands:
        if command[0] == "insert":
            leest.insert(int(command[1]), int(command[2]))

        if command[0] == "print":
            print(leest)

        if command[0] == "remove":
            leest.remove(int(command[1]))

        if command[0] == "append":
            leest.append(int(command[1]))

        if command[0] == "sort":
            leest.sort()

        if command[0] == "pop":
            leest.pop()

        if command[0] == "reverse":
            leest.reverse()

    hash()
    # print(leest)

    s = "string"

    s.find
