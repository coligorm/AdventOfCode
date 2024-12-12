import sys
inFile = sys.argv[1]

with open(inFile,'r') as i:
    lines = i.read().split()

left = []
right = []
dst = []

count = 0
for i in lines:
    if count % 2 != 0:
        right.insert(0,int(i))
    else:
        left.insert(0,int(i))
    count += 1

# right.sort()
# left.sort()

# print(left)
# print(right)

j = 0
for i in left:
    a = i - right[j]
    if a < 0:
        a = a * -1
    dst.insert(0,a)
    j += 1

# total_dst = 0
# for i in dst:
#     total_dst += i
total_dst = sum(dst)

# print(total_dst)

sim = []
for i in left:
    count = 0
    for j in right:
        if i == j:
            count += 1
    sim.insert(0,count*i)

print(sum(sim))