'''Repeated Transactions Delection'''

transactions = input("Enter transactions: ").split()

for t in transactions:
    if transactions.count(t) > 1:
        print("Repeated Transaction:", t)
        transactions = [x for x in transactions if x != t]
    print(transactions)
