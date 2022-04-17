import heapq
def longest_valid_path(orders):
    pickups = {}
    dils = {}
    hp = []
    start = 0
    long_path = []
    for idx, order in enumerate(orders):
        if not order[1] in dils and ((order[0] == 'P' and not order[1] in pickups) or (order[0] == 'D' and order[1] in pickups)):
            if order[0] == 'P':
                pickups[order[1]] = idx
                heapq.heappush(hp, (idx, order[1]))
            else:
                dils[order[1]] = idx
                if len(dils) == len(pickups) and len(long_path) < idx - start + 1:
                    long_path = orders[start: idx + 1]
        else:
            invalidate_idx = idx
            if order[1] in dils:
                invalidate_idx = dils[order[1]]
            elif order[1] in pickups:
                invalidate_idx = pickups[order[1]]

            while hp and hp[0][0] <= invalidate_idx:
                p_idx, o_num = heapq.heappop(hp)
                d_idx = dils[o_num] if o_num in dils else -1
                invalidate_idx = max(p_idx, invalidate_idx, d_idx)
                del pickups[o_num]
                if o_num in dils:
                    del dils[o_num]

            start = invalidate_idx + 1
            if order[0] == 'P':
                pickups[order[1]] = idx
                heapq.heappush(hp, (idx, order[1]))

    return long_path


P1 = "P1"
P2 = "P2"
D1 = "D1"
D2 = "D2"
print(longest_valid_path([P1, P1, D1]))
print(longest_valid_path([P1, P1, D1, D1]))
print(longest_valid_path([P1, D2, D1, P2]))
print(longest_valid_path([P1, D1]))