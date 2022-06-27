import pprint
accounts = {"a":1500, "b":1500, "c":1500}
while 1:
    print("Welcome to Monopoly Calculator")
    opp = input("What would you like to do?: ")
    player = opp[0]
    operation = opp[1]
    amount = int(opp[2:])
    if operation == "-":
        amount *= -1
    accounts[player] = accounts[player] + amount
    pprint.pprint(accounts)
    print("Thank you for your transaction\n-*-")