# Demo: Sum Expenses

expenses = [10.50, 8, 5, 15, 20, 5, 3]

# For loop option:
# sum = 0
# for x in expenses:
#   sum = sum + x

total = 0
expenses = []
num_expenses = int(input("Enter the # of expenses: "))

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)  # Python's built-in sum function

print("You spent $", total, sep="")
