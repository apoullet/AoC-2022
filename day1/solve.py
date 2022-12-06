answers = [sum(sorted(list(map(lambda x: sum(map(int, x.split(' '))), ' '.join(list(map(str.strip, open('input.txt', 'r').readlines()))).split('  '))), reverse=True)[:i+1]) for i in [0, 2]]

print("Part 1:", answers[0])
print("Part 2:", answers[1])
