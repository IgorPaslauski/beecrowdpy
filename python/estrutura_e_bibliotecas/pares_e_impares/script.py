n = int(input())
pares = []
inpares = []

for num in range(n):
    i = int(input())
    if(i % 2 == 0):
        pares.append(i)
    else:
        inpares.append(i)

pares.sort()

inpares.sort(reverse=True)

for num in pares:
    print(num)
for num in inpares:
    print(num)