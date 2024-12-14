import sys

def compare(x,y):
    if 0 < abs((x - y)) <= 3 :
        return True

def is_increasing_or_decreasing(l):
    return l == sorted(l) or l == sorted(l, reverse = True)

def is_safe(l):
    safe = False
    i = 0
    while i < len(l)-1:
        if compare(l[i], l[i+1]) and is_increasing_or_decreasing(l):
            safe = True
        else:
            safe = False
            break
        
        i+=1

    return safe


def main():
    safe_count = 0

    for i in list_of_lists:
        if is_safe(i):
            print(i,":",is_safe(i))
            safe_count+=1

    print(safe_count," reports are safe")



if __name__ == "__main__":
    # inFile = sys.argv[1]
    list_of_lists = []
    with open('test.txt','r') as file:
        for line in file:
            line = line.split()
            if line:
                line = [int(i) for i in line]
                list_of_lists.append(line)

    print("Input:",list_of_lists)

    main()