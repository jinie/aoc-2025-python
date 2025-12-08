#!/usr/bin/env python3
from itertools import chain

def parse_input(text: str):
    return [
        [tuple(map(int, part.split('-'))) for part in line.split(',')]
        for line in text.strip().splitlines()
    ]

def _solve(ranges):
    part1 = part2 = 0
    for start, end in chain.from_iterable(ranges):
        for n in range(start, end + 1):
            s = str(n)
            L = len(s)

            if L % 2 == 0 and s[: L // 2] == s[L // 2 :]:
                part1 += n

            if any(L % k == 0 and s[:k] * (L // k) == s for k in range(1, L // 2 + 1)):
                part2 += n
    return part1, part2

if __name__ == "__main__":
    with open("day2_test.txt") as f:
        test_ranges = parse_input(f.read())
        sol = _solve(test_ranges)
        assert sol[0] == 1227775554
        assert sol[1] == 4174379265

    with open("day2_input.txt") as f:
        ranges = parse_input(f.read())
        sol = _solve(ranges)
        print("Part 1:", sol[0])
        print("Part 2:", sol[1])