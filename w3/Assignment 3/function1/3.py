def solve(nheads,nlegs):
    rabbit = nlegs/2 - nheads
    chicken = nheads - rabbit
    return chicken,rabbit

nheads = int(input())
nlegs = int(input())
print(solve(nheads,nlegs))