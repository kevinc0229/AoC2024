import re

def read_input(filename):
    list = []
    for line in open(filename):
        list.append(line)
    return list
def part1(input):
    res = 0
    pattern = r"mul\((\d+),(\d+)\)"

    for line in input:
        matches = re.findall(pattern, line)
        for num1,num2 in matches:
            res += int(num1) * int(num2)

    return res

def part2(input):
    res = 0
    do = True
    pattern = r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)"

    for line in input:
        matches = []

        for match in re.finditer(pattern, line):
            if match.group(1) and match.group(2):
                matches.append((match.group(1), match.group(2)))
                res += int(match.group(1)) * int(match.group(2)) if do else 0
            else:
                matches.append(match.group(0))
                do = True if match.group(0) == "do()" else False

    return res

if __name__ == '__main__':
    filename = "input.txt"
    list = read_input(filename)

    print(f"part1 result: {part1(list)}")
    print(f"part2 result: {part2(list)}")
