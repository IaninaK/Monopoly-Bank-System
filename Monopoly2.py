a = 1700  #starter stats should equal 1500
b = 1700
c = 1700
while 1:
    print("Welcome to Monopoly Calculator")
    opp = input("What would you like to do?: ")
    if opp[1] == "+":
        if opp[0] == "a":
            a += int(opp[2:])
        elif opp[0] == "b":
            b += int(opp[2:])
        elif opp[0] == "c":
            c += int(opp[2:])
    if opp[1] == "-":
        if opp[0] == "a":
            a -= int(opp[2:])
        elif opp[0] == "b":
            b -= int(opp[2:])
        elif opp[0] == "c":
            c -= int(opp[2:])
    print(f"a = ${a}")
    print(f"b = ${b}")
    print(f"c = ${c}")
    stats = f"""
    ~~
    a = ${a}
    b = ${b}
    c = ${c}
    ~~
    """
    with open(f'monopoly_stats.txt', 'w') as stats_file:
        stats_file.write(stats)
    print("Thank you for your transaction\n-*-")