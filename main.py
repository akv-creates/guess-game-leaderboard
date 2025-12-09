import random

def load_leaderboard(filename="highscore.txt"):
    leaderboard = []
    try:
        with open(filename, "r") as f:
            for line in f:
                name, score = line.strip().split(",")
                leaderboard.append((name, int(score)))
    except FileNotFoundError:
        pass
    return leaderboard

def save_leaderboard(leaderboard, filename="highscore.txt"):
    with open(filename, "w") as f:
        for name, score in leaderboard:
            f.write(f"{name},{score}\n")

def display_leaderboard(leaderboard):
    print("\n🏆 Leaderboard:")
    for i, (name, score) in enumerate(leaderboard, start=1):
        print(f"{i}. {name} - {score} attempts")

def play_game():
    username = input("Enter your name: ")
    secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    while guess != secret_number:
        attempts += 1
        try:
            guess = int(input("Guess The Number! "))
        except ValueError:
            print("⚠ Please enter a valid number!")
            continue

        if guess > secret_number:
            print("Enter a smaller number")
        elif guess < secret_number:
            print("Enter a bigger number")

    print(f"\nCongrats {username}, You Won the Game! 🎉")
    print(f"You guessed {secret_number} in {attempts} attempts")

    return username, attempts

def update_leaderboard(leaderboard, username, attempts):
    leaderboard.append((username, attempts))
    leaderboard = sorted(leaderboard, key=lambda x: x[1])[:5]
    save_leaderboard(leaderboard)
    return leaderboard


def main():
    leaderboard = load_leaderboard()
    username, attempts = play_game()
    leaderboard = update_leaderboard(leaderboard, username, attempts)
    display_leaderboard(leaderboard)


if __name__ == "__main__":
    main()
