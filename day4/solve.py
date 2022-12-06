answer1 = sum(map(int,[*map(lambda x:not (len((set(range(x[0][0],x[0][1]+1))-set(range(x[1][0],x[1][1]+1)))) and len((set(range(x[1][0],x[1][1]+1))-set(range(x[0][0],x[0][1]+1))))),[*map(lambda s:[*map(lambda p:[*map(int,p.split('-'))],s.split(','))],open('input.txt').read().split('\n'))])]))
print("Part 1:", answer1)
answer2 = sum(map(int,[*map(lambda x:len(set(range(x[0][0],x[0][1]+1))&set(range(x[1][0],x[1][1]+1)))>0,[*map(lambda s:[*map(lambda p:[*map(int,p.split('-'))],s.split(','))],open('input.txt').read().split('\n'))])]))
print("Part 2:", answer2)