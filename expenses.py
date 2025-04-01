# Demo: Sum Expenses

expenses = [10.50, 8, 5, 15, 20, 5, 3]

# For loop option:
# sum = 0
# for x in expenses:
#   sum = sum + x

total = sum(expenses) # Python's built-in sum function

print("You spent $", total, sep='')