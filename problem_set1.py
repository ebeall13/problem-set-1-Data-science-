def main():
    print("this is the main function where all functions are run")
    blue()
    blastoff()

def blue():
    red = 3
    purple = 3 * 12
    print(purple)

def blastoff():
    count = int(input("Give me a number: "))
    while count > 0:
        print(count)
        count = count - 1
    print("blastoff!!")

if __name__ == '__main__':
    main()
