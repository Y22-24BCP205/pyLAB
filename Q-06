with open('file1.txt') as f1, open('file2.txt') as f2, open('merged.txt', 'w') as f3:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    maxlen = max(len(lines1), len(lines2))

    for i in range(maxlen):
        if i < len(lines1):
            f3.write(lines1[i])
        if i < len(lines2):
            f3.write(lines2[i])
