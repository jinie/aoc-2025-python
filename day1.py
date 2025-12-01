def part1(instr, start=50, length=100):
    return sum(not (start := (start + (1 if m[0]=='R' else -1)*int(m[1:])) % length)
               for m in instr)


def part2(instructions, start=50, length=100):
    scount = 0

    for ins in instructions:
        d = 1 if ins[0] == 'R' else -1
        steps = int(ins[1:])

        eff = start if d == 1 else (length - start) % length
        scount += (eff + steps) // length

        start = (start + d * steps) % length

    return scount

def main():
    input = open("day1.txt").read().strip().splitlines()
    print("Part 1:", part1(input, 50))
    print("Part 2:", part2(input, 50))

main()