def main():
    print("this is the main function where all functions are run")
    blue()
    blastoff()
    print("total cost of all candy: $" , candy_shop())
    fruit_pricing()
#function blue assigns int value 3 to red, then multiples it by 12 and saves it in purple. Then prints purple
def blue():
    red = 3
    purple = 3 * 12
    print(purple)

#asks the user for a number then counts down from that number and prints blastoff!
def blastoff():
    count = int(input("Give me a postive number: "))
    while count > 0:
        print(count)
        count = count - 1
    print("blastoff!!")

#function that has a list of candy, adds kitkat to that list, inserts skittles at 1, sorts the list, removes kitkat, prints the list
def candy_shop():
    candies = ["gummy worms", "twix", "mints"]
    candies.append("kitkat")
    candies.insert(1, "skittles")
    candies.sort()
    candies.remove("kitkat")
    print(candies)
#creates a new, empty list, adds 3 candies input from the user, adds the old candy list and this list into another list, prints the length, aprints each item in a new line, then returns out the total cost if each item was $1.25
    user_candies = []
    user_candies.append(input("What is one of your favorite candies?"))
    user_candies.append(input("What is another of your favorite candies?"))
    user_candies.append(input("What is one more of your favorite candies?"))
    all_candies = candies.copy() + user_candies.copy()
    print(len(all_candies))
    for candy in all_candies:
        print(candy)
    return 1.25 * len(all_candies)

#a function that contains a dictonary of fruits and their prices as keys
def fruit_pricing():
    fruits = { "apple": 0.75, "banana": 1.25, "orange": 0.80, "peach": 2.25, "coconut": 2.80}
#adds pear to the dictionary, then cost of a peach is printed
    fruits['pear'] = 1.15
    print("The cost of a peach is $" , fruits.get("peach"))
#prints all the fruits over #1.25
    for fruit in fruits:
        if fruits.get(fruit) >= 1.25:
            print(fruit)
#finds the total cost of 3 apples, 2 bananas, a coconut and prints it
    total = 0
    total = total + (3 *(fruits.get("apple")))
    total = total + (2 * (fruits.get("banana")))
    total = total + fruits.get("coconut")
    print("The total cost the of the shopping trip is $", total)
if __name__ == '__main__':
    main()
