#Day 2 MINI PROJECT
# Ishat Noor Mahi. 3006

## SCENARIO 1 ###
def main():
    # fruits = int(input("Enter Fruits: "))
    baskets = int(input("Enter Number of baskets: "))
    print(f"Total Fruits: {details(baskets)}")
    
def is_lucky(fruits):
    return fruits%2!=0

def details(baskets):
    total = 0
    for i in range(1,baskets+1):

        fruits = int(input(f"How many fruits in basket-{i}?: "))
        print(f"basket {i} has {fruits} fruits")

        if is_lucky(fruits):
            print(f"basket {i} is lucky")

        total = total+fruits

    return total

# main()


## SCENARIO 2 ###

def start():
    rows = int(input("Enter Row Number:"))
    seats = int(input("Enter Seats Per Row:"))

    print_seats(rows,seats)

def print_seats(rows,seats):
    for row in range(1,rows+1):
        for seat in range(1,seats+1):
            print(f"{row} x {seat}")

# start()


for i in range(25):
    print(f"{i}.")