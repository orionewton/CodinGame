import sys
import math


def log(*x):
    print(" == ", x, file=sys.stderr, flush=True)


def convert(n, maya, ln, h):
    if len(n) == ln * h:
        return maya.get(n)
    digit = len(n) // (ln * h)
    res = ''
    for i in range(digit):
        a = i*ln*h
        b = i*ln*h + ln*h
        num = n[a:b]
        tmp = maya.get(num)
        res += base(tmp)
    ans = 0
    n = len(res)-1
    for i in range(len(res)):
        ans = ans + int(rebase(res[i])) * 20**n
        n -= 1
    return ans


def compute(n1, n2, op):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    return int(n1 / n2)


def display(res, nums, h):
    for i in range(h):
        print(nums[res][i])


def base(num):
    if num == 10:
        return 'A'
    if num == 11:
        return 'B'
    if num == 12:
        return 'C'
    if num == 13:
        return 'D'
    if num == 14:
        return 'E'
    if num == 15:
        return 'F'
    if num == 16:
        return 'G'
    if num == 17:
        return 'H'
    if num == 18:
        return 'I'
    if num == 19:
        return 'J'
    if num == 20:
        return 'K'
    return str(num)


def rebase(num):
    if num == 'A':
        return 10
    if num == 'B':
        return 11
    if num == 'C':
        return 12
    if num == 'D':
        return 13
    if num == 'E':
        return 14
    if num == 'F':
        return 15
    if num == 'G':
        return 16
    if num == 'H':
        return 17
    if num == 'I':
        return 18
    if num == 'J':
        return 19
    if num == 'K':
        return 20
    return int(num)


def disp_nums(res, nums, h):
    q = res
    r = ''
    while q > 0:
        tmp = str(q % 20)
        if int(tmp) > 9:
            tmp = base(int(tmp))
        r = tmp + r
        q = q // 20
    let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    for i in r:
        if i in let:
            i = rebase(i)
        display(int(i), nums, h)


l, h = [int(i) for i in input().split()]
numeral = []
maya = {}
for i in range(h):
    numeral.append(input())
# for i in numeral:
#    log(i)
nums = []
for i in range(20):
    tmp = ''
    num = []
    for j in range(h):
        tmp += numeral[j][i*l:i*l+l]
        num.append(numeral[j][i*l:i*l+l])
    nums.append(num)
    maya[tmp] = i

# log(maya)
n1 = ''
s1 = int(input())
for i in range(s1):
    n1 += input()

n2 = ''
s2 = int(input())
for i in range(s2):
    n2 += input()

# log(n1)
# log(n2)
n1 = convert(n1, maya, l, h)
n2 = convert(n2, maya, l, h)
operation = input()
log(n1, operation, n2)
res = compute(n1, n2, operation)
log(res)
if res < 20:
    display(res, nums, h)
else:
    disp_nums(res, nums, h)
