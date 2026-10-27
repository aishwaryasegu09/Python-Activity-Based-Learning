'''Nested Loop Examination Seating Generator'''

rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        print(f"R{i}S{j}", end=" ")
    print()