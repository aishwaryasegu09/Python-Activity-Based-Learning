'''Multi-Event Sports Scheduling and Scoring'''

n = int(input("Enter number of events: "))
events = []

for i in range(n):
    name = input("Enter event name: ")
    score = int(input("Enter score: "))
    events.append((name, score))

events.sort(key=lambda x: x[1], reverse=True)

print("Event Results:")
for name, score in events:
    print(name, ":", score)