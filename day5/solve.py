from functools import reduce

answers = ["".join([*map(lambda f:f[-1],reduce(lambda a,c:a[:int(c[5])-1]+[a[int(c[5])-1]+a[int(c[3])-1][-(int(c[1])):][::t]]+a[int(c[5]):int(c[3])-1]+[a[int(c[3])-1][:-(int(c[1]))]]+a[int(c[3]):] if int(c[3])>int(c[5]) else a[:int(c[3])-1]+[a[int(c[3])-1][:-(int(c[1]))]]+a[int(c[3]):int(c[5])-1]+[a[int(c[5])-1]+a[int(c[3])-1][-(int(c[1])):][::t]]+a[int(c[5]):],(st:=[*map(lambda r:[*filter(lambda s:bool(s.strip()),[*map(lambda l:l[r],cr)])][::-1],range(len(cr:=[*map(lambda p:[*map(lambda q:q[1::4],p.split('\n'))][:-1],[(ins:=open('input.txt').read().split('\n\n'))[0]])][0]+(mv:=ins[1].split('\n'))[0:0])*0+len(cr[0])))])[0:0]+[*map(lambda m:m.split(" "),mv)],st))]) for t in [-1,1]]
print("Part 1:", answers[0])
print("Part 2:", answers[1])