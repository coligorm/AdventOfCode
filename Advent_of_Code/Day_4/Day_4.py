import numpy as np

def check_horizontal(line):
    if xmas in line:
        return True

def check_backwards(line):
    if xmas[::-1] in line:
        return True

def check_down(x,pos,word_search):
    row = pos[0]+1
    col = pos[1]
    pos = (row,col)
    x+=1
    letter = xmas[x:][0]
    
    # print("looking down here for",letter,"...",pos)
    if row > len(word_search)-1:
        # print("Out of Bounds...")
        pass
    elif letter == 'S' and letter == word_search[row][col]:
        
        occurances.append("XMAS")
        print("!!! XMAS FOUND",occurances.count("XMAS"))
    elif letter == word_search[row][col]:
        print("Found:",letter,pos)
        check_down(x,(row,col),word_search)

def check_up(x,pos,word_search):
    row = pos[0]-1
    col = pos[1]
    pos = (row,col)
    x+=1
    letter = xmas[x:][0]
    
    # print("looking up here for",letter,"...",pos)
    if row < 0:
        # print("Out of Bounds...")
        pass
    elif letter == 'S' and letter == word_search[row][col]:
        
        occurances.append("XMAS")
        print("!!! XMAS FOUND",occurances.count("XMAS"))
    elif letter == word_search[row][col]:
        print("Found:",letter,pos)
        check_up(x,(row,col),word_search)

def check_left_up_diag(x,pos,word_search):
    row = pos[0]-1
    col = pos[1]-1
    pos = (row,col)
    x+=1
    letter = xmas[x:][0]
    
    # print("looking left_up here for",letter,"...",pos)
    if row < 0 or col < 0:
        # print("Out of Bounds...")
        pass
    elif letter == 'S' and letter == word_search[row][col]:
        
        occurances.append("XMAS")
        print("!!! XMAS FOUND",occurances.count("XMAS"))
    elif letter == word_search[row][col]:
        print("Found:",letter,pos)
        check_left_up_diag(x,(row,col),word_search)

def check_left_down_diag(x,pos,word_search):
    row = pos[0]+1
    col = pos[1]-1
    pos = (row,col)
    x+=1
    letter = xmas[x:][0]
    
    # print("looking left_down here for",letter,"...",pos)
    if row > len(word_search)-1 or col < 0:
        # print("Out of Bounds...")
        pass
    elif letter == 'S' and letter == word_search[row][col]:
        
        occurances.append("XMAS")
        print("!!! XMAS FOUND",occurances.count("XMAS"))
    elif letter == word_search[row][col]:
        print("Found:",letter,pos)
        check_left_down_diag(x,(row,col),word_search)

def check_right_up_diag(x,pos,word_search):
    row = pos[0]-1
    col = pos[1]+1
    pos = (row,col)
    x+=1
    letter = xmas[x:][0]

    # print("looking right_up here for",letter,"...",pos)
    if row < 0 or col > len(word_search[row])-1:
        # print("Out of Bounds...")
        pass
    elif letter == 'S' and letter == word_search[row][col]:
        
        occurances.append("XMAS")
        print("!!! XMAS FOUND",occurances.count("XMAS"))
    elif letter == word_search[row][col]:
        print("Found:",letter,pos)
        check_right_up_diag(x,(row,col),word_search)

def check_right_down_diag(x,pos,word_search):
    row = pos[0]+1
    col = pos[1]+1
    pos = (row,col)
    x+=1
    letter = xmas[x:][0]
    
    # print("looking right_down here for",letter,"...",pos)
    if row > len(word_search)-1 or col > len(word_search[row])-1 :
        # print("Out of Bounds...")
        pass
    elif letter == 'S' and letter == word_search[row][col]:
        
        occurances.append("XMAS")
        print("!!! XMAS FOUND",occurances.count("XMAS"))
    elif letter == word_search[row][col]:
        print("Found:",letter,pos)
        check_right_down_diag(x,(row,col),word_search)

def main():
    print(word_search)
    count = 0
    row = 0
    col = 0
    pos = (0,0)

    for row, line in enumerate(word_search):
        print("\n",line,"\n____")
        if check_horizontal(line):
            occurances.append("XMAS")
            print("!!! XMAS FOUND frontwards",occurances.count("XMAS"))
        if check_backwards(line):
            occurances.append("XMAS")
            print("!!! XMAS FOUND backwards",occurances.count("XMAS"))
        # print("row",row, "line",line)
        
        for col, letter in enumerate(line):
            pos = (row,col)
            # print(pos)
            if letter == 'X':
                pos = (row,col)
                print("X is here:",pos)
                check_left_up_diag(0,pos,word_search)
                check_left_down_diag(0,pos,word_search)
                check_right_up_diag(0,pos,word_search)
                check_right_down_diag(0,pos,word_search)
                check_up(0,pos,word_search)
                check_down(0,pos,word_search)
                

    print(occurances.count("XMAS"))
            # if letter in xmas and len(word) < len(xmas):
            #     word = word + letter
            # print(word)
        
        
        
    # print(count)


if __name__ == "__main__":
    # inFile = sys.argv[1]
    word_search = []
    with open('test.txt','r') as file:
        word_search = file.read().split()

    xmas = "XMAS"
    occurances = []

    main()