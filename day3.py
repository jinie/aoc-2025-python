#!/usr/bin/env python3

def parse(path):
    with open(path) as f:
        return [list(map(int, line.strip())) for line in f if line.strip()]

def pick(row, k):
    dp = [0] + [-1]*k
    for d in row:
        for j in range(k, 0, -1):
            if dp[j-1] != -1:
                cand = dp[j-1]*10 + d
                if cand > dp[j]:
                    dp[j] = cand
    return dp[k]

def solve(path, k):
    return sum(pick(r, k) for r in parse(path))

def main():
    assert solve("day3_test.txt", 2)  == 357
    assert solve("day3_test.txt", 12) == 3121910778619
    print("Part 1:", solve("day3_input.txt", 2))
    print("Part 2:", solve("day3_input.txt", 12))

if __name__ == "__main__":
    main()
