def projection(Z, V, s,M,B):
    found = 0 # flag whether extreme points are hit
    # if left slope is smaller than updated slope of sampled point s

    if Z[s - 1] < Z[s]:
        # find maximum i such that average value to right is less than or equal to slope at i-1
        for i in range(s, 0, -1):
            # c is average value to slopes from i to s
            c = 1 / (s - i + 1) * sum(value for key, value in Z.items() if i <= key <= s)
            if Z[i - 1] >= c:
                # if such condition is met, no need to go futher left for averaging
                found = 1
                break
        # updating the slopes from i to s and equating all to same value as c
        # if no left point is found until 1, assign i = 0
        # as slope will update from 1 to s
        if found == 0:
            i = 0
        for j in range(i, s + 1):
            if found == 0:
                # sum from s to i=0
                c = 1 / (s - 0 + 1) * sum(value for key, value in Z.items() if 0 <= key <= s)
                # if i =1, equate to minimum of some large number and average value
                V[j] = min(B, c)
            else:
                V[j] = c

    # if right side point slope is larger than updated slope of sampled point s
    elif Z[s] < Z[s + 1]:
        for i in range(s, M, 1): # from i = s to M-1 is iterated
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
    return V

