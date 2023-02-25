#HackerRank
def runner_up(n, arr):
    new_arr = set()
    for i in arr:
        new_arr.add(i)
    new_arr.remove(max(new_arr))
    runner = max(new_arr)
    if 2 <= n <= 10 and -100 <= runner <= 100:
        print(runner)
    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
runner_up(n, arr)