"""
File: breakeven_sales.py
------------------
How many more you have to sell until you break even?
"""


def main():
    print("HOW MANY MORE YOU HAVE TO SELL TO BREAK-EVEN?")
    current_sales= int(input("Enter your Current Sales: "))
    fixed_costs= int(input("Enter your Fixed Costs: "))
    selling_price= int(input("Enter your Selling Price/Unit: "))
    variable_costs= int(input("Enter your Variable Costs/Unit: "))
    breakeven= fixed_costs/(selling_price - variable_costs)
    sales_you_need= int(breakeven - current_sales)
    if sales_you_need >0:
        print("Aha! You need " + str(sales_you_need) + " more unit sales to break-even.")
    elif sales_you_need <0:
        print("Congr@ts! You're already break-even and you're making profit!")
    elif sales_you_need ==0:
        print("Congr@ts! You're at break-even point. Keep selling more so you can make profits!")







# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
