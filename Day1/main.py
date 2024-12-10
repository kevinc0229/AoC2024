import heapq

def read_input(filename):
    list1, list2 = [], []
    with open(filename, 'r') as f:
        for line in f:
            num1, num2 = line.strip().split()
            list1.append(int(num1))
            list2.append(int(num2))

    return list1, list2

def part1(list1, list2):
    res = 0
    heap1, heap2 = list(list1), list(list2)

    heapq.heapify(heap1)
    heapq.heapify(heap2)

    while heap1 and heap2:
        res += abs(heapq.heappop(heap1) - heapq.heappop(heap2))
    
    return res

def part2(list1, list2):
    res = 0 
    d = {key: 0 for key in list1}

    for num in list2:
        if num in d:
            d[num] += 1
    
    for num in list1:
        res += num * d[num]

    return res

if __name__ == '__main__':
    filename = "input.txt"
    list1, list2 = read_input(filename)

    print(f"part1 result: {part1(list1, list2)}")
    print(f"part2 result: {part2(list1, list2)}")