# hackerrank_Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    integer_tuple = tuple(integer_list)
    integer_hash = hash(integer_tuple)

    print(integer_hash)
