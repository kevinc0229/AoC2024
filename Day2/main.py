def read_input(filename):
    list = []

    for line in open(filename):
        list.append([int(num) for num in line.strip().split(" ")])

    return list

def check_safe(row):
    diff = [row[i]-row[i+1] for i in range(len(row)-1)]      
    inc = True if diff[0] > 0 else False
    
    for d in diff:
        if (inc and d < 0) or (not inc and d > 0) or (abs(d) > 3 or abs(d) < 1):
            return False
        
    return True

def part1(list):
    res = 0
    
    for row in list:
        safe = check_safe(row)
        res += 1 if safe else 0
    
    return res

def part2(list):
    res = 0
    
    for row in list:
        safe = check_safe(row)
        res += 1 if safe else 0

        if not safe:
            for i in range(len(row)):
                truncated = row[:i] + row[i+1:]
                safe = check_safe(truncated)

                if safe:
                    res += 1
                    break

    return res
    
if __name__ == '__main__':
    filename = "input.txt"
    list = read_input(filename)

    print(f"part1 result: {part1(list)}")
    print(f"part2 result: {part2(list)}")
