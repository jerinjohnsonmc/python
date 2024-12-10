""" budget.py: coding with operators demo. """
__author__ = "Jerin Johns"
__contact__ = "L00187577@atu.ie"
__copyright__ = "Copyright $YEAR, JJ"
__date__ = "28NOV24"
__deprecated__ = False
__license__ = "GPLv3"
__status__ = "test"
__version__ = "1"


monthly_allowance = 430
rent_per_week = 80
elctricity_bill_per_month =25
wifi_bill_per_month = 12
groceries_per_month = 80
oil_per_3_month = 170

total_expense = (rent_per_week*4) + (oil_per_3_month/3) + elctricity_bill_per_month + groceries_per_month + wifi_bill_per_month

print ("total" , total_expense)

under_allowance = monthly_allowance > total_expense

print ("is under allowance" , under_allowance)

