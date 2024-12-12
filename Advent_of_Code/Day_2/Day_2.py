import sys
inFile = sys.argv[1]

list_of_lists = []
with open(inFile,'r') as file:
    for line in file:
        line = line.split()
        if line:
            line = [int(i) for i in line]
            list_of_lists.append(line)

print("Input:",list_of_lists)


def compare(x,y):
    if 0 <abs((x - y)) <= 3 :
        return True
    
def is_increasing_or_decreasing(l):
    if l == sorted(l) or l == sorted(l, reverse = True):
        return True


safe_count = 0

for i in list_of_lists:
    if is_increasing_or_decreasing(i):
        j = 0
        safe = False
        while j < len(i)-1:
            if compare(i[j],i[j+1]):
                safe = True
                j+=1
            else:
                safe = False
                break
                
        if safe:
            safe_count += 1
        print(i,":",safe)

print(safe_count," reports are safe")
