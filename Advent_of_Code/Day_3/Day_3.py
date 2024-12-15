import re
import math

def regex(reg, string):
    return re.findall(reg, string)

def mul(instruction):
    digits = regex(extract_nums,instruction)
    nums = [int(x) for x in digits]
    prod = math.prod(nums)

    return prod

def main():
    print("corrupted file =",txt,"\n")
    
    total = 0
    toggle = True
    
    instructions = regex(findInstructions,txt)
    print(instructions,"\n")
    
    for i in instructions:
        if toggle and "mul" in i:
            ans = mul(i)
            total += ans
        
        match i:
            case "don't()":
                toggle = False   
            case "do()":
                toggle = True

    print("Total =",total)


if __name__ == "__main__":
    # inFile = sys.argv[1]
    with open('input.txt','r') as file:
        txt = file.read()

    findInstructions = r"(?:mul\(\d*\,\d*\))|(?:do\(\))|(?:don\'t\(\))"
    extract_nums = r"\d+"

    main()