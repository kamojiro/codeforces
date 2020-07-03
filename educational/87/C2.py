from math import sin, pi, cos
def solve():
    n = int( input())
    return(cos(pi/(4*n))/sin(pi/(2*n)))
    
def main():
    t = int( input())
    print("\n".join( map( str, [ solve() for _ in range(t)])))
if __name__ == '__main__':
    main()
