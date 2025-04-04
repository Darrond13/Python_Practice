#implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due
#Once the user has inputted at least 50 cents, output how many cents in change the user is owed
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
def main():
        amount_due = 50
        coinbank = [25, 10 , 5]

        while amount_due > 0:
                print(f"Amount Due: {amount_due}")

                coin = int(input("Insert Coin: "))
                if coin in coinbank:
                        amount_due -= coin
                else:
                        print("Invalid coin")

        print(f"Change Owed: {abs(amount_due)}")

main()
