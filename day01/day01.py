file = open('input.txt','r')
cals = [0, 0]
elfs = []
top3 = 0

for line in file:
    if line.strip() == '':

        if cals[1] > cals[0]:
            cals[0] = cals[1]

        elfs.append(cals[1])
        cals[1] = 0
    else:
        cals[1] += int(line.strip())

elfs.sort(reverse=True)
print(elfs)
top3 = sum(elfs[0:3])

print('the most calories being carried by an elf is: ', cals[0], max(elfs), top3)


