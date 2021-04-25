t = int(input())

while t:
    t-=1
    r,b = map(int, input().split())
    runs = list(map(int, input().split()) )

    curRuns = 0
    curBalls = 0

    for i in range(b):
        # b wins
        if curRuns + (b-i)*6 < r:
            print("B",curBalls)
            break
        curBalls += 1
        curRuns += runs[i]

        # A wins
        if curRuns >= r:
            print("A",curBalls)
            break
        if curBalls == b and curRuns == r-1:
            print("T",curBalls)
        if curBalls == b and curRuns < r-1:
            print("B",curBalls)
