import re
import math

def regex(reg, string):
    return re.findall(reg, string)

def main():
    print("corrupted file =",txt,"\n")
    
    total = 0

    findMul = r"mul\(\d*\,\d*\)"
    extract_nums = r"\d+"
    
    instructions = regex(findMul,txt)
    count = 0
    for i in instructions:
        count +=1
        digits = regex(extract_nums,i)
        nums = [int(x) for x in digits]

        prod = math.prod(nums)
        total += prod
    print(total)



if __name__ == "__main__":
    # inFile = sys.argv[1]
    with open('input.txt','r') as file:
        txt = file.read()

    main()