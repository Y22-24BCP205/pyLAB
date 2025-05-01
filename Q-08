with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    for line in infile:
        words = line.split()
        filtered = [w for w in words if w.lower() not in ('a', 'an', 'the')]
        outfile.write(' '.join(filtered) + '\n')
