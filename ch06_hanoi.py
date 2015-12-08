def hamoi(n):
    steps = []
    def sub(n, pfrom, pto, pbuf):
        if n == 1:
            steps.append((pfrom, pto))
        else:
            sub(n-1, pfrom, pbuf, pto)
            steps.append((pfrom, pto))
            sub(n-1, pbuf, pto, pfrom)
    sub(n, 'A', 'C', 'B')
    return steps


def simulate_hanoi(n, pfrom, pto, pbuf, steps):
    pillars = {pfrom: list(range(n)), pto: [], pbuf: []}
    for s in steps:
        disk = pillars[s[0]].pop()
        pillars[s[1]].append(disk)
    if (pillars[pfrom] == [] and
        pillars[pbuf] == [] and
        pillars[pto] == list(range(n))):
        return True
    else:
        return False
