import sys

rawin = sys.stdin.read().strip().split()

# part 1

tot = 0
for i in rawin:
    tot += int(i)
print("part 1:", tot)

# part 2

tot2 = 0
freq = set()
freq.add(tot2)
while True:
    for i in rawin:
        tot2 += int(i)
        if tot2 in freq:
            print("part 2:", tot2)
            sys.exit(0)
        freq.add(tot2)
