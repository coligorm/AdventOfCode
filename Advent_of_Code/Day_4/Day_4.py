def main():
    print(txt)

if __name__ == "__main__":
    # inFile = sys.argv[1]
    with open('test.txt','r') as file:
        txt = file.read()

    main()