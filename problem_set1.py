def main():
    print("this is the main function where all functions are run")
    blue()
    blastoff()
    print("total cost of all candy: $" , candy_shop())

def blue():
    red = 3
    purple = 3 * 12
    print(purple)

def blastoff():
    count = int(input("Give me a postive number: "))
    while count > 0:
        print(count)
        count = count - 1
    print("blastoff!!")

def candy_shop():
    candies = ["gummy worms", "twix", "mints"]
    candies.append("kitkat")
    candies.insert(1, "skittles")
    candies.sort()
    candies.remove("kitkat")
    print(candies)
    user_candies = []
    user_candies.append(input("What is one of your favorite candies?"))
    user_candies.append(input("What is another of your favorite candies?"))
    user_candies.append(input("What is one more of your favorite candies?"))
    all_candies = candies.copy() + user_candies.copy()
    print(len(all_candies))
    for candy in all_candies:
        print(candy)
    return 1.25 * len(all_candies)




if __name__ == '__main__':
    main()
