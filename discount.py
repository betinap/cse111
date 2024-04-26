"""Work as a team to write a Python program named discount.py that gets a customer’s subtotal as input and gets
the current day of the week from your computer’s operating system. Your program must not ask the user to enter
the day of the week. Instead, it must get the day of the week from your computer’s operating system.
If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the 
subtotal. Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. Your 
program must print the discount amount if applicable, the sales tax amount, and the total amount due."""

# Import the datetime class from the datetime module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current date and time as a datetime object from the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Asks the user for the subtotal
subtotal = float(input('Please enter the subtotal: '))

if day_of_week == 1 or 2:
    if subtotal >= 50:
        discount = subtotal * 0.10
        sales_tax_amount =(subtotal - discount) * 0.06
        total = subtotal* 0.90 + sales_tax_amount
        print(f'Discount amount: {discount:.2f}')
        print(f'sales amount {sales_tax_amount:.2f}')
        print(f'Total: {total:.2f}')
    else:
        sales_tax_amount = subtotal * 0.06
        total = subtotal + sales_tax_amount
        print(f'Sales tax amount: {sales_tax_amount:.2f}')
        print(f'Total: {total:.2f}')
else:
    sales_tax_amount = subtotal * 0.06
    total = subtotal + sales_tax_amount
    print()
    print(f'Sales tax amount: {sales_tax_amount:.2f}')
    print(f'Total: {total:.2f}')

