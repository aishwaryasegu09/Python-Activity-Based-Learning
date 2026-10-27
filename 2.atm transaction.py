'''ATM Transaction Sequence Simulation'''

balance = 5000
amount = int(input("Enter withdrawal amount: "))

if amount > 0 and amount <= balance:
    balance -= amount
    print("Withdrawn:", amount)
    print("Balance:", balance)
else:

    print("Invalid transaction")
