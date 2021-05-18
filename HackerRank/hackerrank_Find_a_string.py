# hackerrank Find a string


def count_substring(string, sub_string):
    return len([i for i in range(len(string)) if string.startswith(sub_string, i)])


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


# test
# from https://www.geeksforgeeks.org/python-all-occurrences-of-substring-in-string/


string = "ABCDCDCDC"
sub_string = "CDC"

occurences = 0
for i in range(len(string)):
    if string.startswith(sub_string, i):
        occurences += 1

print(occurences)

len([i for i in range(len(string)) if string.startswith(sub_string, i)])


#####
