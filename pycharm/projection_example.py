# projection algorithm
# sampled decision point
import copy
B = 10  # some big number
#s = s
#Z = Z  # intermediate slope
found = 0
s = 2
Z = {}
Z[0] = 2
Z[1] = 1
Z[2] = 2
Z[3] = -1
Z[4] = -2
M = 4
V = copy.copy(Z)
print(V)
if Z[s - 1] < Z[s]:
    for i in range(s, 0, -1):
        #c = 1 / (s - i + 1) * sum(Z[i:s + 1])
        c = 1 / (s - i + 1) * sum(value for key, value in Z.items() if i <= key <= s)
        if Z[i - 1] >= c:
            found = 1
            break
    if found == 0:
        i = 0

    for j in range(i, s + 1):
        if found == 0:
            # sum to rom s to i=1
            c = 1 / (s - 0 + 1) * sum(value for key, value in Z.items() if 0 <= key <= s)
            # if i =1, equate to minimum of some large number and average value
            V[j] = min(B, c)
        else:
            V[j] = c
elif Z[s] < Z[s + 1]:
    for i in range(s, M, 1):  # from i = s to M-1 is iterated
        c = 1 / (i - s + 1) * sum(value for key, value in Z.items() if s <= key <= i)
        if Z[i + 1] <= c:
            found = 1
            break
if found == 0:
    i = M
# updating slopes of points (s,i) to average value
for j in range(s, i + 1):
    if found == 0:
        # sum to from s to i= M
        c = 1 / (M - s + 1) * sum(value for key, value in Z.items() if s <= key <= M)
        V[j] = max(-B, c)
    else:
        V[j] = c
else:
    None

print(V)
