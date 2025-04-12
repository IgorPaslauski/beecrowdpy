T = int(input())
A,B,C,D,E = map(int, input().split())

R = 0

if A == T:
    R+=1
if B == T:
    R+=1
if C == T:
    R+=1
if D == T:
    R+=1
if E == T:
    R+=1
print(f"{R}")