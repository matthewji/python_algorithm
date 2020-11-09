# coding=utf-8
# my solution
def solution(number, k):
    i, count = 0, 0
    while True:
        if int(number[i]) < int(number[i+1]):
            number = number[:i] + number[i+1:]
            count += 1
            i = 0
        else:
            i += 1
        if count == k:
            break

    return number
# Status: Timeout
# Note: 가장 큰 문제는 i를 0으로 돌려서 다시 처음부터 체크하게 하는 부분이다. number 가 최대 1000000자리이기 때문에 타임아웃 당하는 테스트케이스가 생긴다
#       그렇다고 -= 1 로 하면 number = number[] + number[] 부분과 상충해서 문제가 생긴다. 다른 방법을 강구해봐야 할 듯하다.


# my solution 2
def solution(number, k):
    count, i = 0, 0
    while count < k and i + 1 < len(number):
        if number[i] < number[i + 1]:
            number = number[:i] + number[i + 1:]
            count += 1
            i = max(i - 1, 0)
        else:
            i += 1

    return number[:count - k] if count < k else number
# Status: Accepted
# Algorithm: Greedy
# Note: 위의 코드와 사실상 같다. i -= 1 부분이 i가 음수로 넘어갈 경우 문제가 생기는 걸 확인하고 max(i - 1, 0)으로 해결해줬다.
#       맨 마지막에 if count < k 부분을 추가 코드없이 return 안에 녹여서 썼다.


# 다른 사람들 풀이에서 stack을 활용한 걸 봤다. 스택을 써서 한번 더 풀어보자.

