lst = [3, 5, 7, 8, 1, 6, 8, 4, 8, 14, 5, 9, 5, 1, 2, 9]

print(max(set(sorted(lst)), key=lst.count))
print(max(sorted(lst), key=lst.count))
