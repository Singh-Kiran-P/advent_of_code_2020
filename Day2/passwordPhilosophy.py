import re
print(sum([(p[int(i) - 1] == l) ^ (p[int(j) - 1] == l) for i, j, l, p in re.findall(r'(\d+)-(\d+) (\w): (\w+)', open('Day2/input.txt').read())]))
