def main():
    print("this is the main function where all functions are run")
    blue()
    blastoff()
    print("total cost of all candy: $" , candy_shop())
    fruit_pricing()

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

def fruit_pricing():
    fruits = { "apple": 0.75, "banana": 1.25, "orange": 0.80, "peach": 2.25, "coconut": 2.80}
    fruits['pear'] = 1.15
    print("The cost of a peach is $" , fruits.get("peach"))
    for fruit in fruits:
        if fruits.get(fruit) >= 1.25:
            print(fruit)
    total = 0
    total = total + (3 *(fruits.get("apple")))
    print(total)
    total = total + (2 * (fruits.get("banana")))
    print(total)
    total = total + fruits.get("coconut")
    print(total)
    print("The total cost the of the shopping trip is $", total)
if __name__ == '__main__':
    main()
