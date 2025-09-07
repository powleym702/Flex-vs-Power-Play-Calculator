import math
from scipy.optimize import root, root_scalar

def breakpct_finder():
    while True:
        user_input = input("How many props will be in your lineup? ")
        if user_input.isdigit() and int(user_input) >= 2 and int(user_input) <= 6: 
            numberofprops = int(user_input)
            break
        elif not user_input.isdigit():
            print("Error: Please enter a whole number between 2 and 6.")
        elif int(user_input) < 2:
            print("Error: You need at least two props to make a lineup!")
        else:
            print("Error: The maximum amount of props for a lineup is 6!")
    while True:
        lineup_input = input("Will it be a flex play or a power play? ").lower()
        if lineup_input.__contains__("flex"):
            lineup_type = 1
            break
        elif lineup_input.__contains__("power"):
            lineup_type = 2
            break
        else:
            print("Error: Please enter power or flex! ")
    if lineup_type == 2:               
        payout = float(input("What is the payout? (i.e., for 6x, enter 6): "))
        breakpct = round(((1/payout) ** (1/numberofprops)) * 100, 2)
    if lineup_type == 1:
        if numberofprops == 2:
            print("You need at least 3 props for a flex lineup!") 
        else:
            first_payout = input(f"What is the payout for winning all {numberofprops} props? (i.e., for 6x, enter 6) ")
            second_payout = input(f"What is the payout for winning {numberofprops-1} props? (i.e., for 6x, enter 6) ")
            p1 = float(first_payout) - 1
            p2 = float(second_payout) - 1
        if numberofprops == 5 or numberofprops == 6:
            third_payout = input(f"What is the payout for winning {numberofprops-2} props? (i.e., for 6x, enter 6) ")
            p3 = float(third_payout) - 1
        if numberofprops == 3:
            f = lambda x: (p1 - 3*p2 - 2) * x**3 + (3 + p2*3) * x**2 - 1
            sol = root(f, x0=0.5)
            breakpct = round(100*sol.x[0],2)
        elif numberofprops == 4:
            f = lambda x: (p1-4*p2-3)*x**4 + (4*p2+4)*x**3 - 1
            sol = root_scalar(f, bracket=[0,1], method='brentq')
            breakpct = round(100*sol.root,2)
        elif numberofprops == 5:
            f = lambda x: (p1-5*p2+10*p3+6)*x**5 + (5*p2-20*p3-15)*x**4 + (10*p3+10)*x**3 - 1
            sol = root_scalar(f, bracket=[0,1], method='brentq', xtol=1e-10)
            breakpct = round(100*sol.root,2)
        elif numberofprops == 6:
            f = lambda x: (p1-6*p2+15*p3+10)*x**6 + (6*p2-30*p3-24)*x**5 + (15*p3+15)*x**4 - 1
            sol = root_scalar(f, bracket=[0,1], method='brentq', xtol=1e-10)
            breakpct = round(100*sol.root,2)

    print(f"Individual Prop Breakeven percentage: {breakpct}%")

breakpct_finder()