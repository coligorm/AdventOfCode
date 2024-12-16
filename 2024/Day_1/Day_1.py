import sys
inFile = sys.argv[1]

with open(inFile,'r') as i:
    lines = i.read().split()

left = []
right = []
dst = []

# if the number is odd, add to the right list
# if the number is even, add to the left list

count = 0
for i in lines:
    if count % 2 != 0:
        right.insert(0,int(i))
    else:
        left.insert(0,int(i))
    count += 1

# sort in order to compare distance between left nad right list
right.sort()
left.sort()

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

# add all numbers is dst list to find answer to part one
print(total_dst)

# count each the occurance of each number in left list within the right list
# multiply left list number with the count and add to similarity score list
sim = []
for i in left:
    count = 0
    for j in right:
        if i == j:
            count += 1
    sim.insert(0,count*i)

# answer for part two
print(sum(sim))