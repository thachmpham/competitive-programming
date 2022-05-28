# uva 11392 Binary*3 Type Multiple
import sys
from collections import deque

# version 1: TLE
# def bfs(k):
#     q = deque()
#     q.appendleft(3)
#
#     while True:
#         n = q.pop()
#
#         if n % k == 0:
#             return n
#
#         if n % 10 == 0:
#             q.appendleft(n * 10 + 3)
#             q.appendleft(n*10)
#         else:
#             q.appendleft(n * 10 + 3)


# version 2: Out of memory
# def bfs(k):
#     q = deque()
#     q.appendleft((3, '3'))
#
#     while True:
#         (n, s) = q.pop()
#
#         if n % k == 0:
#             return n, s
#
#         # (a*b) % k = (a%k * b%k) % k
#         # n0 = 10n
#         # n0 % k= 10n % k = (10%k * n%k) % k
#         n0 = ((10 % k) * (n % k)) % k
#
#         # (a+b) % k = (a%k + b%k) % k
#         # n3 = 10n + 3
#         # n3 % k= (10n + 3) % k = (10n % k + 3 % k) % k = (10%k + n%k) % k + 3%k) % k
#         n3 = (((n % k) * (10 % k)) % k + 3 % k) % k
#
#         if s[-1] == '0':
#             q.appendleft((n3, s + '3'))
#         else:
#             q.appendleft((n3, s + '3'))
#             q.appendleft((n0, s + '0'))


# version 3: TLE
'''
def bfs(k):
    q = deque()
    q.appendleft((3, '3', 0, 1))  # (n, last_digit, number of 0's, number of 3's

    while True:
        (n, last, count0, count3) = q.pop()

        if n % k == 0:
            return n, last, count0, count3

        # (a*b) % k = (a%k * b%k) % k
        # n0 = 10n
        # n0 % k= 10n % k = (10%k * n%k) % k
        n0 = ((10 % k) * (n % k)) % k

        # (a+b) % k = (a%k + b%k) % k
        # n3 = 10n + 3
        # n3 % k= (10n + 3) % k = (10n % k + 3 % k) % k = (10%k + n%k) % k + 3%k) % k
        n3 = (((n % k) * (10 % k)) % k + 3 % k) % k

        if last == '0':
            q.appendleft((n3, '3', count0, count3+1))
        else:
            q.appendleft((n3, '3', count0, count3+1))
            q.appendleft((n0, '0', count0+1, count3))
'''


def bfs(k):
    # find a pair X = 3...3 (x digits), Y = 3...3 (y digits),
    # such that:
    #               X mod k == Y mod k
    # then:
    #               (X - Y) mod k == 0

    ''' bfs(k=8)
    length:     1   2   3       4
    n:          3   33  333     3333
    n mod 8:    3   1   5       5

    3333 mod 8 = 5
    333  mod 8 = 5
    --> (3333 - 333) mod 8 = 0
    -->  3000
    --> count3 = 1, count0 = 3
    '''

    n = 3
    length = 1

    mod_to_len = {}

    while True:
        if n % k == 0:
            return length, length, 0

        if n in mod_to_len:
            count0s = mod_to_len[n]
            count3s = length - count0s
            return length, count3s, count0s

        mod_to_len[n % k] = length

        # n3 = 10n + 3
        # n3 % k= (10n + 3) % k = (10n % k + 3 % k) % k = (10%k + n%k) % k + 3%k) % k
        n3 = (((n % k) * (10 % k)) % k + 3 % k) % k

        n = n3
        length += 1

# main
while True:
    s = sys.stdin.readline()

    if s == '':
        break

    k = int(s)
    (a,b,c) = bfs(k)
    print(a,b,c)