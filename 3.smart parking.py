'''Smart Parking Fee Management'''

hours = int(input("Enter parking hours: "))

if hours <= 2:
    fee = 30
else:
    fee = 30 + (hours - 2) * 10

print("Parking Fee:", fee)