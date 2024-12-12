TARGET_XMAS = "XMAS"
TARGET_X_MAS = set(["MAS", "SAM"])

def read_input(filename):
    res = []
    for line in open(filename):
        res.append(list(line.strip()))
    return res

def count_XMAS_sequences(m,n,i,j,grid):
    ct = 0
    directions = [
        (-1,-1),
        (-1,0),
        (-1,1),
        (0,-1),
        (0,1),
        (1,-1),
        (1,0),
        (1,1)
    ]

    for dx,dy in directions:
        curr = 0

        for k in range(len(TARGET_XMAS)):
            ni,nj = i+dx*k, j+dy*k

            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == TARGET_XMAS[k]:
                curr += 1

        if curr == len(TARGET_XMAS):
            ct += 1

    return ct

def count_X_MAX_sequences(m,n,i,j,grid):
    cross1 = [
        (-1,-1),
        (0,0),
        (1,1)
    ]
    cross2 = [
        (-1,1),
        (0,0),
        (1,-1)
    ]
    curr1 = ""
    curr2 = ""

    for dx,dy in cross1:
        ni,nj = i+dx, j+dy

        if 0 <= ni < m and 0 <= nj < n:
            curr1 += grid[ni][nj]
    for dx,dy in cross2:
        ni,nj = i+dx, j+dy

        if 0 <= ni < m and 0 <= nj < n:
            curr2 += grid[ni][nj]

    return 1 if curr1 in TARGET_X_MAS and curr2 in TARGET_X_MAS else 0

def part1(grid):
    res = 0
    m,n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "X":
                res += count_XMAS_sequences(m,n,i,j,grid)
    
    return res

def part2(grid):
    res = 0
    m,n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "A":
                res += count_X_MAX_sequences(m,n,i,j,grid)
    
    return res

if __name__ == '__main__':
    filename = "input.txt"
    grid = read_input(filename)

    print(f"part1 result: {part1(grid)}")
    print(f"part2 result: {part2(grid)}")