# 03/05 금요일

# 사칙연산 - 사칙연산

# 사칙연산 - 곱셈

# if문 - 알람 시계

# while 문 - 더하기 사이클

# 03/06 토요일

# 1차원 배열 - 평균은 넘겠지

# 함수 - 셀프넘버

# 문자열 - 단어공부

# 문자열 - 크로아티아 알파벳

# 03/08 월요일

# 기본 수학 1 - 달팽이는 올라가고 싶다

# 기본 수학 1 - ACM 호텔

# 기본 수학 2 - 소수 구하기

# 03/08 월요일

# 알고리즘 강의 1주차

# 최대값 찾기

# 최빈값 찾기

# 알고리즘 강의 2주차

# 더하거나 빼거나

# 03/09 화요일

# 재귀 - 하노이 탑 이동 순서

# 정렬 - 좌표 정렬하기 2

# 이분탐색 - 나무 자르기

# 03/10 수요일

# 스택 - 균형잡힌 세상

# 스택 - 스택 수열

string_list = []

bracket = {
  ')':'(',
  ']':'['
}

while True :
  string = list(input())
  if string[-1] == '.' and len(string) == 1 :
    break
  string_list += [string]

def check_balance(string) :
  stack = []
  for s in string :
    if s in bracket.values() :
      stack.append(s)
    elif not stack and s in bracket :
      return "no"
    elif s in bracket and stack[-1] == bracket[s] :
      stack.pop()
    elif s in bracket :
      return "no"
    
  if not stack :
    return "yes"
  else :
    return "no"

for string in string_list :
  print(check_balance(string))

# 큐 - 회전하는 큐

# 03/11 목요일

# DFS와 BFS - 바이러스

# DFS와 BFS - 토마토

# 동적계획법 - 피보나치 함수

# 동적계획법 - 가장 긴 증가하는 부분 수열