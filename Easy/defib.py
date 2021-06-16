import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def log(x):
    print(x, file=sys.stderr, flush=True)


lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())
defib = []
for i in range(n):
    defib.append(input().split(';'))
dist = []
for i in defib:
    lon2 = float(i[4].replace(',', '.'))
    lat2 = float(i[5].replace(',', '.'))
    x = (lon2 - lon) * math.cos((lat+lat2)/2)
    y = lat2 - lat
    d = math.sqrt(x*x + y*y) * 6371
    dist.append(d)

i = dist.index(min(dist))
# Write an answer using print

print(defib[i][1])
