'''Haackathon Team Formation and Ranking'''

n = int(input("Enter number of teams: "))
teams = []

for i in range(n):
    name = input("Enter team name: ")
    score = int(input("Enter score: "))
    teams.append((name, score))

teams.sort(key=lambda x: x[1], reverse=True)

print("Team Rankings:")
for i, team in enumerate(teams, 1):
    print(i, team[0], team[1])