import random

#setting leaderboard
leaderboard = []
try:
    with open("highscore.txt", "r") as f:
        for line in f:
            name, score = line.strip().split(",")
            leaderboard.append((name, int(score)))
except:
    leaderboard = []

# initialisation of variables

username = input("Enter your name: ")
n = random.randint(1, 100)
a = -1
guesses = 0

#game loop

while n != a:
    guesses += 1
    a = int(input("Guess The Number! "))

    if a > n:
        print("Enter a smaller number")
    elif a < n:
        print("Enter a bigger number")

# update leaderboard
leaderboard.append((username, guesses))
leaderboard = sorted(leaderboard, key=lambda x: x[1])[:5]  # keep top 5 players

with open("highscore.txt", "w") as f:
    for name, score in leaderboard:
        f.write(f"{name},{score}\n")

print("\n🏆 Leaderboard:")
for i, (name, score) in enumerate(leaderboard, start=1):
    print(f"{i}. {name} - {score} attempts")

print(f"\nCongrats {username}, You Won the Game! 🎉")
print(f"You guessed {n} in {guesses} attempts")
