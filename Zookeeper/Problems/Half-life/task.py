N = int(input())
R = int(input())
i = N
T = 0
while i > R:
    i /= 2
    T += 12
print(T)
