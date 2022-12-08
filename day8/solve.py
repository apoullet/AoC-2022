with open('input.txt', 'r') as pzlIn:
    sq = [*(map(lambda w: [*map(int, w)], map(str.strip, pzlIn.readlines())))]

count = 2*(len(sq)-2+len(sq[0]))
for row in range(1, len(sq)-1):
    print()
    for col in range(1, len(sq[row])-1):
        curh = sq[row][col]
        print(curh, end='')
        visible = False
        idx = 1
        while sq[row-idx][col]<curh:
            if row-idx == 0:
                count+=1
                visible = True
                break
            idx-=1
        if (visible):
            continue
        idx = 1
        while sq[row][col+idx]<curh:
            if col+idx == len(sq[row])-1:
                count+=1
                visible = True
                break
            idx+=1
        if (visible):
            continue
        idx = 1
        while sq[row+idx][col]<curh:
            if row+idx == len(sq)-1:
                count+=1
                visible = True
                break
            idx+=1
        if (visible):
            continue
        idx = 1
        while sq[row][col-idx]<curh:
            if col-idx == 0:
                count+=1
                break
            idx-=1

print("Part 1:", count)