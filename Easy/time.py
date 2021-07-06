import sys
import math
from datetime import datetime


def log(*x):
    print(" == ", x, file=sys.stderr, flush=True)


begin = input()
end = input()
begin = datetime.strptime(begin, '%d.%m.%Y').date()
end = datetime.strptime(end, '%d.%m.%Y').date()
log(begin)
log(end)
tot = end - begin
D = tot.days
Y = D // 365
years = ""
if Y == 1:
    years = "1 year, "
elif Y > 1:
    years = str(Y) + " years, "
M = (D % 365) // 30
log(M)
if end.day < begin.day and begin.month > end.month:
    M -= 1
months = ""
if M == 1:
    months = "1 month, "
elif M > 1:
    months = str(M) + " months, "

if Y == 0 and M == 1 and D < 31:
    months = ""

print(years + months + "total " + str(D) + " days")
