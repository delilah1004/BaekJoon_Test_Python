# 03/15 월요일

# DFS - 조합 구하기

# 집합
a = [1,2,3,4,5]
# 집합의 길이
n = len(a)
# 조합의 길이
num = 3

def dfs(level, start, res) :
  if level == num :
    print(res)
    return
  for i in range(start, len(a)) :
    dfs(level+1, i+1, res+str(a[i]))

dfs(0, 0, "")