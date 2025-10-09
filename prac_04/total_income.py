"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    """Display income report for incomes over a given number of months."""
    incomes = [] # Stores the income for each month
    months = int(input("How many months? ")) # number of income inputs

    # get the income for the number of specified months
    for month in range(1, months + 1):
        income = float(input(f"Enter income for month {month}")) # Uses f-string instead of string concatenation
        incomes.append(income)

    # Prints the output from the list
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]     # retrieve income for each month
        total += income                 # Update the total
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()