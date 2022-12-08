with (open('input.txt', 'r')) as pzlIn:
    lines = map(str.strip, pzlIn.readlines())

wd, fs = [], []
for line in lines:
    if line.startswith('$ ls'):
        continue

    if line.startswith('$ cd'):
        if '..' in line:
            wd = wd[:-1]
        else:
            wd += [line.split(' ')[-1]]
            fs += [[''.join(wd)]]
        continue
    
    fs[-1] += [line.split(' ')[int('dir' in line)]]

fss = {}
for d in fs[::-1]:
    fss[d[0]] = sum(map(lambda ds: int(ds) if ds.isdigit() else fss[d[0]+ds], d[1:]))

print("Part 1:", sum(filter(lambda ds: ds<100_000, fss.values())))
print("Part 2:", sorted(filter(lambda ds: ds>8_381_165, fss.values()))[:])