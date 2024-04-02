def getcntvotes(i, voters, suffixsum, level):
    l = 0
    r = len(voters) - 1
    while l < r:
        m = (l + r) // 2
        if voters[m][0] < level:
            l = m + 1
        else:
            r = m
    if voters[l][0] < level:
        return 0
    cntvotes = suffixsum[l] - level * (len(voters) - l)
    if voters[i][0] >= level:
        cntvotes -= voters[i][0] - level
    return cntvotes


def model(voters, i, suffixsum):
    l = 0
    r = 10**6
    while l < r:
        level = (l + r + 1) // 2
        cntvotes = getcntvotes(i, voters, suffixsum, level)
        if cntvotes + voters[i][0] > level:
            l = level
        else:
            r = level - 1

    cntvotes = getcntvotes(i, voters, suffixsum, l)
    recovery = max(0, voters[i][0] + cntvotes - l - 2)
    return cntvotes - recovery, l, recovery


if __name__ == "__main__":
    with open("input.txt", "r") as reader:
        n = int(reader.readline().strip())
        p = [0] * n
        voters = [0] * n
        for i in range(n):
            v, p[i] = map(int, reader.readline().strip().split(" "))
            voters[i] = (v, i)

    voters.sort()
    suffixsum = [0] * n
    suffixsum[-1] = voters[-1][0]
    for i in range(n - 2, -1, -1):
        suffixsum[i] = suffixsum[i + 1] + voters[i][0]

    mincost = 10**6 + 10**6 * 10**6 + 1
    for i in range(n):
        if p[voters[i][1]] != -1:
            cost, level, recovery = model(voters, i, suffixsum)
            if p[voters[i][1]] + cost < mincost:
                mincost = p[voters[i][1]] + cost
                ans = [i, cost, level, recovery]

    winner, cost, level, recovery = ans
    resvotes = [0] * n
    for i in range(n):
        if i == winner:
            resvotes[voters[i][1]] = voters[i][0] + cost
        elif voters[i][0] <= level:
            resvotes[voters[i][1]] = voters[i][0]
        else:
            if recovery > 0:
                resvotes[voters[i][1]] = level + 1
                recovery -= 1
            else:
                resvotes[voters[i][1]] = level

    with open("output.txt", "w") as file:
        file.write(str(mincost) + "\n")
        file.write(str(voters[winner][1] + 1) + "\n")
        file.write(" ".join(str(votes) for votes in resvotes))
