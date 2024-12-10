import heapq

def read_input(filename):
    list1, list2 = [], []
    with open(filename, 'r') as f:
        for line in f:
            num1, num2 = line.strip().split()
            list1.append(int(num1))
            list2.append(int(num2))

    return list1, list2

def main(list1, list2):
    res = 0

    heapq.heapify(list1)
    heapq.heapify(list2)

    while list1 and list2:
        res += abs(heapq.heappop(list1) - heapq.heappop(list2))
    
    return res

if __name__ == '__main__':
    filename = "input.txt"
    list1, list2 = read_input(filename)

    print(main(list1, list2))