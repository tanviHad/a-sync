l1 = [3, 6, 9, 12, 15, 18, 21] 
l2 = [4, 8, 12, 16, 20, 24, 28]

l3 = []

for i in range(len(l1)):
    if i % 2 == 0:
        l3.append(l1[i])
    else:
        l3.append(l2[i])

print(l3)