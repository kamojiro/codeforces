from collections import deque, Counter
def solve():
    S = list( map( int, list( input().strip())))
    C = Counter(S)
    if C[1] > 0 and C[2] > 0 and C[3] > 0:
        ans = C[1] + C[2] + C[3]
    else:
        return(0)
    nums = [0]*4
    d = deque()
    for s in S:
        d.append(s)
        nums[s] += 1
        while d:
            if nums[d[0]] > 1:
                nums[d.popleft()] -= 1
            else:
                break
        if nums[1] > 0 and nums[2] > 0 and nums[3] > 0:
            if sum( nums) < ans:
                ans = sum( nums)
    return( ans)

    
def main():
    t = int( input())
    print("\n".join( map( str, [ solve() for _ in range(t)])))
if __name__ == '__main__':
    main()
