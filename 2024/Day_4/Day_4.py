def check_horizontal(line):
    if xmas in line:
        print("XMAS FOUND FOREWARD")
        print(line.count(xmas))
        return line.count(xmas)
    else:
        return 0

def check_backwards(line):
    if xmas[::-1] in line:
        print("XMAS FOUND BACKWARD")
        print(line.count(xmas[::-1]))
        return line.count(xmas[::-1])
    else:
        return 0

def check_down(x,pos,word_search):
    row = pos[0]+1
    col = pos[1]
    pos = (row,col)
    x+=1
    letter = xmas[x:][0]
    
    if row > len(word_search)-1:
        print("Out of Bounds...")
        pass
    elif letter == 'S' and letter == word_search[row][col]:
        print("Found:",letter,pos)
        print("!!! XMAS FOUND !!!")
        return True
    elif letter == word_search[row][col]:
        print("Found:",letter,pos)
        if check_down(x,(row,col),word_search): return True
        return False

def check_up(x,pos,word_search):
    row = pos[0]-1
    col = pos[1]
    pos = (row,col)
    x+=1
    letter = xmas[x:][0]
    
    if row < 0:
        print("Out of Bounds...")
        pass
    elif letter == 'S' and letter == word_search[row][col]:
        print("Found:",letter,pos)
        print("!!! XMAS FOUND !!!")
        return True
    elif letter == word_search[row][col]:
        print("Found:",letter,pos)
        if check_up(x,(row,col),word_search): return True
        return False

def check_left_up_diag(x,pos,word_search):
    row = pos[0]-1
    col = pos[1]-1
    pos = (row,col)
    x+=1
    letter = xmas[x:][0]
    
    if part_one:    
        if row < 0 or col < 0:
            # print("Out of Bounds...")
            pass
        elif letter == 'S' and letter == word_search[row][col]:
            print("Found:",letter,pos)
            print("!!! XMAS FOUND !!!")
            return True
        elif letter == word_search[row][col]:
            print("Found:",letter,pos)
            if check_left_up_diag(x,(row,col),word_search): return True
            return False
    
    # PART TWO
    else:
        if row < 0 or col < 0:
            # print("Out of Bounds...")
            pass
        elif letter == 'M' and letter == word_search[row][col]:
            print("Found:",letter,pos)
            # Reset (row,col) to centre postion of 'X' a.k.a pos of found A
            # in order to search the opposite direction
            row = pos[0]+1
            col = pos[1]+1
            if check_right_down_diag(x+1,(row,col),word_search): return True
            return False 
        elif letter == 'S' and letter == word_search[row][col]:
            print("Found:",letter,pos)
            print("!!! XMAS FOUND !!!")
            return True

def check_left_down_diag(x,pos,word_search):
    row = pos[0]+1
    col = pos[1]-1
    pos = (row,col)
    x+=1
    letter = xmas[x:][0]
    
    if part_one:    
        if row > len(word_search)-1 or col < 0:
            # print("Out of Bounds...")
            pass
        elif letter == 'S' and letter == word_search[row][col]:
            print("Found:",letter,pos)
            print("!!! XMAS FOUND !!!")
            return True
        elif letter == word_search[row][col]:
            print("Found:",letter,pos)
            if check_left_down_diag(x,(row,col),word_search): return True
            return False
    
    # PART TWO
    else:
        if row > len(word_search)-1 or col < 0:
            # print("Out of Bounds...")
            pass
        elif letter == 'M' and letter == word_search[row][col]:
            print("Found:",letter,pos)
            # Reset (row,col) to centre postion of 'X' a.k.a pos of found A
            # in order to search the opposite direction
            row = pos[0]-1
            col = pos[1]+1
            if check_right_up_diag(x+1,(row,col),word_search): return True
            return False 
        elif letter == 'S' and letter == word_search[row][col]:
            print("Found:",letter,pos)
            print("!!! XMAS FOUND !!!")
            return True

def check_right_up_diag(x,pos,word_search):
    row = pos[0]-1
    col = pos[1]+1
    pos = (row,col)
    x+=1
    letter = xmas[x:][0]
    
    if part_one:
        if row < 0 or col > len(word_search[row])-1:
            # print("Out of Bounds...")
            pass
        elif letter == 'S' and letter == word_search[row][col]:
            print("Found:",letter,pos)
            print("!!! XMAS FOUND !!!")
            return True
        elif letter == word_search[row][col]:
            print("Found:",letter,pos)
            if check_right_up_diag(x,(row,col),word_search): return True
            return False
    
    # PART TWO
    else:
        if row < 0 or col > len(word_search[row])-1:
            # print("Out of Bounds...")
            pass
        elif letter == 'M' and letter == word_search[row][col]:
            print("Found:",letter,pos)
            # Reset (row,col) to centre postion of 'X' a.k.a pos of found A
            # in order to search the opposite direction
            row = pos[0]+1
            col = pos[1]-1
            if check_left_down_diag(x+1,(row,col),word_search): return True
            return False 
        elif letter == 'S' and letter == word_search[row][col]:
            print("Found:",letter,pos)
            print("!!! XMAS FOUND !!!")
            return True

def check_right_down_diag(x,pos,word_search):
    row = pos[0]+1
    col = pos[1]+1
    pos = (row,col)
    x+=1
    letter = xmas[x:][0]
    
    if part_one:    
        if row > len(word_search)-1 or col > len(word_search[row])-1 :
            # print("Out of Bounds...")
            pass
        elif letter == 'S' and letter == word_search[row][col]:
            print("Found:",letter,pos)
            print("!!! XMAS FOUND !!!")
            return True
        elif letter == word_search[row][col]:
            print("Found:",letter,pos)
            if check_right_down_diag(x,(row,col),word_search): return True
            return False
    
    # PART TWO
    else:
        if row > len(word_search)-1 or col > len(word_search[row])-1 :
            # print("Out of Bounds...")
            pass
        elif letter == 'M' and letter == word_search[row][col]:
            print("Found:",letter,pos)
            # Reset (row,col) to centre postion of 'X' a.k.a pos of found A
            # in order to search the opposite direction
            row = pos[0]-1
            col = pos[1]-1
            if check_left_up_diag(x+1,(row,col),word_search): return True
            return False 
        elif letter == 'S' and letter == word_search[row][col]:
            print("Found:",letter,pos)
            print("!!! XMAS FOUND !!!")
            return True

def main():
    print(word_search)
    count = 0
    row = 0
    col = 0
    pos = (0,0)

    for row, line in enumerate(word_search):
        print("\n",line,"\n____")

        if part_one:
            count += check_horizontal(line)
            count += check_backwards(line)

            for col, letter in enumerate(line):
                pos = (row,col)
                if letter == 'X':
                    pos = (row,col)
                    print("X is here:",pos)
                    if check_left_up_diag(0,pos,word_search): count += 1
                    if check_left_down_diag(0,pos,word_search): count += 1
                    if check_right_up_diag(0,pos,word_search): count += 1
                    if check_right_down_diag(0,pos,word_search): count += 1
                    if check_up(0,pos,word_search): count += 1
                    if check_down(0,pos,word_search): count += 1
        ### PART TWO ### 
        else:
            for col, letter in enumerate(line):
                pos = (row,col)
                if letter == 'A':
                    print("A is here:",pos)
                    # FIND M
                    if check_left_up_diag(0,pos,word_search) and check_left_down_diag(0,pos,word_search): 
                        count += 1
                        print(count)
                    if check_left_up_diag(0,pos,word_search) and check_right_up_diag(0,pos,word_search):
                        count += 1
                        print(count)
                    if check_left_down_diag(0,pos,word_search) and check_right_down_diag(0,pos,word_search):
                        count += 1
                        print(count)
                    if check_right_up_diag(0,pos,word_search) and check_right_down_diag(0,pos,word_search):
                        count += 1
                        print(count)

    print("FINAL COUNT:",count)


if __name__ == "__main__":
    # inFile = sys.argv[1]
    word_search = []
    with open('input.txt','r') as file:
        word_search = file.read().split()

    xmas = "XMAS"
    part_one = False

    main()