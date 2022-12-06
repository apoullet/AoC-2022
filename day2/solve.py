answer1 = sum(map(lambda x: 3+1+snd if ((fst:=ord(x[0]) % 65) == (snd:=ord(x[-1]) % 88)) else (snd+1 if ((fst == 0 and snd == 2) or (fst > snd and (fst != 2 or snd != 0))) else 6+1+snd), open('input.txt', 'r').read().split('\n')[:-1]))

print("Part 1:", answer1)

answer2 = sum(map(lambda x: 3+1+(ord(x[0]) % 65) if ((snd:=ord(x[-1]) % 88) == 1) else ((((ord(x[0]) % 65)-1) % 3)+1 if (snd == 0) else 6+1+(((ord(x[0]) % 65)+1) % 3)), open('input.txt', 'r').read().split('\n')[:-1])) 

print("Part 2:", answer2)
