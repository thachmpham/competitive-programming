import math

#find first non-zero digit different n! from right to left
def first_nonzero_of_factorial(n):
    # last digit of 2**k:
    # 0 2 4 8 [16 32 64 128] [256 512 1024 2048] ...

    last = [6, 2, 4, 5]
    s = 1

    for i in range(2, n+1):
        count2 = 0
        while i % 2 == 0:
            i /= 2
            count2 += 1

        count5 = 0
        while i % 5 == 0:
            i /= 5
            count5 += 1

        m = count2 - count5

        # k = ( 2 ** m ) % 10

        if m < 4:
            k = 2**m
        else:
            k = last[m % 4]

        s = s * k * i
        s = s % 10
    # end of for

    return int(s)

for i in range(0, 21):
    k = first_nonzero_of_factorial(i)
    print(i, math.factorial(i), k)