answer1 = sum(map(lambda m:ord(m)-64-int(m.islower())*6,[*map(str.swapcase,[*map(lambda l:[*set(l[len(l)//2:])&set(l[:len(l)//2])][0],open('input.txt').read().split('\n'))])]))
print("Part 1:", answer1)
answer2 = sum(map(lambda m:ord(m)-64-int(m.islower())*6,[*map(str.swapcase,[*map(lambda g:[*set(g[0])&set(g[1])&set(g[2])][0],[*zip(l:=open('input.txt').read().split('\n')[:],l[1:],l[2:])][::3])])]))
print("Part 2:", answer2)