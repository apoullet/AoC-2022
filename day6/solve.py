answers = [[*map(lambda i:False if i < (j-1) else len(set([*s[i-(j-1):i+1]]))==j,range(len(s:=open('input.txt').read())))].index(True)+1 for j in [4, 14]]
print("Part 1:", answers[0])
print("Part 2:", answers[1])