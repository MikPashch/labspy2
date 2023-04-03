# 1_1 exercise

from math import sqrt

a = [10, 5, 24, 4]    # list
a_a = []

a_max = max(a)  # max of list a
a_min = min(a)  # min of list a
u = (sum(a)) / len(a)  # middle of list a

# sequence standard deviation in "a" list - further "ssd"

for i in a:
    x = (i - u)**2
    a_a.append(x)

ssd = sqrt(sum(a_a) / len(a))   # sequence standard deviation in "a" list

print(str(round(ssd, 3)) + " end")

